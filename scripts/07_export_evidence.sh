#!/usr/bin/env bash
set -euo pipefail

mkdir -p evidence
TS=$(date +%Y%m%d-%H%M%S)
OUT="evidence/evidence-${TS}.txt"

{
  echo "# Evidencia automática - $TS"
  echo
  echo "## Git"
  git status --short || true
  git log --oneline -n 10 || true
  echo
  echo "## Docker compose ps"
  docker compose ps || true
  echo
  echo "## Contenedores"
  docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}' || true
  echo
  echo "## Puertos locales"
  ss -tulpn 2>/dev/null || netstat -tulpn 2>/dev/null || true
  echo
  echo "## Pruebas HTTP"
  for url in http://localhost:8080 http://localhost:3000 http://localhost:5000/health http://localhost:8081; do
    echo "### $url"
    curl -I --max-time 10 "$url" || true
    echo
  done
} | tee "$OUT"

echo "Evidencia guardada en $OUT"
