#!/usr/bin/env bash
set -euo pipefail

echo "== Deteniendo laboratorio sin borrar volúmenes =="
docker compose down

echo "Para borrar todo, incluida la base de datos: docker compose down -v"
