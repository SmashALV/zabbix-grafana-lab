#!/usr/bin/env python3
"""Escaneo básico y seguro de hosts/puertos para práctica de networking.

Usar solo sobre redes propias, laboratorio local o infraestructura autorizada.
"""
import argparse
import ipaddress
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed


def check_port(ip: str, port: int, timeout: float = 0.7) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((ip, port)) == 0


def scan_host(ip: str, ports: list[int]) -> tuple[str, list[int]]:
    open_ports = []
    for port in ports:
        if check_port(ip, port):
            open_ports.append(port)
    return ip, open_ports


def main():
    parser = argparse.ArgumentParser(description="Escaneo TCP simple para laboratorio autorizado")
    parser.add_argument("--network", default="127.0.0.1/32", help="Red CIDR. Ej: 192.168.1.0/24")
    parser.add_argument("--ports", default="22,80,443,3000,5000,8080,8081,10050,10051", help="Puertos separados por coma")
    parser.add_argument("--workers", type=int, default=32)
    args = parser.parse_args()

    network = ipaddress.ip_network(args.network, strict=False)
    ports = [int(p.strip()) for p in args.ports.split(",") if p.strip()]

    print(f"Escaneando {network} puertos {ports}")
    print("Usar solo en redes propias o autorizadas.\n")

    hosts = [str(ip) for ip in network.hosts()] or [str(network.network_address)]
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = [ex.submit(scan_host, ip, ports) for ip in hosts]
        for fut in as_completed(futures):
            ip, open_ports = fut.result()
            if open_ports:
                print(f"{ip}: abiertos {open_ports}")

if __name__ == "__main__":
    main()
