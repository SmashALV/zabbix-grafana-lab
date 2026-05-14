#!/usr/bin/env bash
set -euo pipefail

if [ ! -f .env ]; then
  echo "No existe .env. Creando desde .env.example"
  cp .env.example .env
fi

echo "== Construyendo e iniciando laboratorio =="
docker compose up -d --build

echo "\n== Estado de contenedores =="
docker compose ps

echo "\nURLs:"
echo "Zabbix:  http://localhost:8080  usuario: Admin / clave: zabbix"
echo "Grafana: http://localhost:3000  usuario: admin / clave: admin123"
echo "App:     http://localhost:5000/health"
echo "Nginx:   http://localhost:8081"

echo "\nSugerencia: espera 2 a 5 minutos y luego ejecuta scripts/03_zabbix_api_bootstrap.py"
