#!/usr/bin/env python3
"""Alta inicial de hosts y escenarios web en Zabbix usando JSON-RPC.

Uso:
  python scripts/03_zabbix_api_bootstrap.py

Variables opcionales:
  ZBX_URL=http://localhost:8080/api_jsonrpc.php
  ZBX_USER=Admin
  ZBX_PASSWORD=zabbix
"""
import os
import sys
import time
import json
import requests
from typing import Any, Dict, List, Optional

ZBX_URL = os.getenv("ZBX_URL", "http://localhost:8080/api_jsonrpc.php")
ZBX_USER = os.getenv("ZBX_USER", "Admin")
ZBX_PASSWORD = os.getenv("ZBX_PASSWORD", "zabbix")
GROUP_NAME = os.getenv("ZBX_GROUP", "Autoaprendizaje Observabilidad")

class ZabbixAPIError(RuntimeError):
    pass

class ZabbixAPI:
    def __init__(self, url: str):
        self.url = url
        self.auth: Optional[str] = None
        self.req_id = 0

    def call(self, method: str, params: Any) -> Any:
        self.req_id += 1
        payload: Dict[str, Any] = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": self.req_id,
        }
        if self.auth:
            payload["auth"] = self.auth
        r = requests.post(self.url, json=payload, timeout=30)
        r.raise_for_status()
        data = r.json()
        if "error" in data:
            raise ZabbixAPIError(json.dumps(data["error"], indent=2, ensure_ascii=False))
        return data.get("result")

    def login(self, user: str, password: str) -> None:
        # Zabbix 6+ usa "username". Algunas versiones antiguas aceptaban "user".
        try:
            self.auth = self.call("user.login", {"username": user, "password": password})
        except ZabbixAPIError:
            self.auth = self.call("user.login", {"user": user, "password": password})

    def get_or_create_group(self, name: str) -> str:
        groups = self.call("hostgroup.get", {"filter": {"name": [name]}, "output": ["groupid", "name"]})
        if groups:
            return groups[0]["groupid"]
        result = self.call("hostgroup.create", {"name": name})
        return result["groupids"][0]

    def find_template(self, candidates: List[str]) -> Optional[str]:
        for name in candidates:
            templates = self.call("template.get", {"filter": {"host": [name]}, "output": ["templateid", "host", "name"]})
            if templates:
                return templates[0]["templateid"]
            templates = self.call("template.get", {"search": {"name": name}, "output": ["templateid", "host", "name"]})
            if templates:
                return templates[0]["templateid"]
        return None

    def get_or_create_host(self, host: str, groupid: str, templates: Optional[List[str]] = None, dns: Optional[str] = None, ip: str = "127.0.0.1") -> str:
        existing = self.call("host.get", {"filter": {"host": [host]}, "output": ["hostid", "host"]})
        if existing:
            return existing[0]["hostid"]

        params: Dict[str, Any] = {
            "host": host,
            "groups": [{"groupid": groupid}],
        }
        if templates:
            params["templates"] = [{"templateid": tid} for tid in templates]
        if dns:
            params["interfaces"] = [{
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": dns,
                "port": "10050"
            }]
        else:
            params["interfaces"] = [{
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": ip,
                "dns": "",
                "port": "10050"
            }]
        result = self.call("host.create", params)
        return result["hostids"][0]

    def ensure_web_scenario(self, hostid: str, name: str, url: str, status_codes: str = "200") -> None:
        tests = self.call("httptest.get", {"hostids": hostid, "filter": {"name": [name]}, "output": ["httptestid", "name"]})
        if tests:
            print(f"OK: escenario web ya existe: {name}")
            return
        self.call("httptest.create", {
            "name": name,
            "hostid": hostid,
            "delay": "1m",
            "retries": 1,
            "steps": [{
                "name": "GET principal",
                "url": url,
                "status_codes": status_codes,
                "no": 1,
                "timeout": "10s"
            }]
        })
        print(f"OK: escenario web creado: {name} -> {url}")

def wait_for_zabbix(api: ZabbixAPI, retries: int = 30) -> None:
    for i in range(1, retries + 1):
        try:
            api.login(ZBX_USER, ZBX_PASSWORD)
            return
        except Exception as exc:
            print(f"Esperando Zabbix ({i}/{retries}): {exc}")
            time.sleep(10)
    raise SystemExit("Zabbix no respondió a tiempo. Verifica docker compose ps y logs.")

def main() -> int:
    print(f"Conectando a {ZBX_URL} como {ZBX_USER}")
    api = ZabbixAPI(ZBX_URL)
    wait_for_zabbix(api)

    groupid = api.get_or_create_group(GROUP_NAME)
    print(f"OK: grupo listo: {GROUP_NAME} ({groupid})")

    linux_template = api.find_template([
        "Linux by Zabbix agent",
        "Template OS Linux by Zabbix agent",
        "Linux by Zabbix agent active"
    ])
    templates = [linux_template] if linux_template else []
    if linux_template:
        print(f"OK: template Linux encontrado: {linux_template}")
    else:
        print("ADVERTENCIA: no se encontró template Linux. Puedes asociarlo manualmente en Zabbix.")

    agent_hostid = api.get_or_create_host("LAB - Docker Agent2", groupid, templates=templates, dns="zabbix-agent2")
    print(f"OK: host Agent2 listo: {agent_hostid}")

    py_hostid = api.get_or_create_host("LAB - Python App", groupid, dns="python-app")
    api.ensure_web_scenario(py_hostid, "Python App Healthcheck", "http://python-app:5000/health")

    nginx_hostid = api.get_or_create_host("LAB - Nginx", groupid, dns="sample-nginx")
    api.ensure_web_scenario(nginx_hostid, "Nginx Healthcheck", "http://sample-nginx:80/")

    print("\nListo. Revisa Zabbix > Data collection > Hosts y Monitoring > Latest data.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
