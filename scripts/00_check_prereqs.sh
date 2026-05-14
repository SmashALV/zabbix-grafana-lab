#!/usr/bin/env bash
set -euo pipefail

echo "== Validando prerrequisitos =="

check_cmd() {
  if command -v "$1" >/dev/null 2>&1; then
    echo "OK: $1 -> $($1 --version 2>/dev/null | head -n 1 || true)"
  else
    echo "FALTA: $1"
    return 1
  fi
}

check_cmd docker
check_cmd git || true
check_cmd python3

if docker compose version >/dev/null 2>&1; then
  echo "OK: docker compose -> $(docker compose version)"
else
  echo "FALTA: Docker Compose v2"
  exit 1
fi

echo "\nRecursos del sistema:"
if command -v free >/dev/null 2>&1; then free -h; fi
if command -v df >/dev/null 2>&1; then df -h .; fi

echo "\nValidación finalizada."
