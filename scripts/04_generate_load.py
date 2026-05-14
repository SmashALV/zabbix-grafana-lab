#!/usr/bin/env python3
"""Genera tráfico HTTP y carga CPU controlada sobre la app Flask del laboratorio."""
import argparse
import time
import urllib.request
import urllib.error


def get(url: str) -> int:
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            r.read()
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        print(f"ERROR: {url}: {e}")
        return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://localhost:5000", help="URL base de la app")
    parser.add_argument("--requests", type=int, default=30, help="Número de requests")
    parser.add_argument("--cpu-seconds", type=int, default=5, help="Segundos de carga CPU por ciclo")
    args = parser.parse_args()

    print(f"Generando tráfico sobre {args.url}")
    for i in range(1, args.requests + 1):
        path = "/health" if i % 5 else f"/cpu?seconds={args.cpu_seconds}"
        status = get(args.url.rstrip("/") + path)
        print(f"{i:03d} {path} -> HTTP {status}")
        time.sleep(1)

    print("Listo. Revisa Zabbix/Grafana después de 1 a 3 minutos.")

if __name__ == "__main__":
    main()
