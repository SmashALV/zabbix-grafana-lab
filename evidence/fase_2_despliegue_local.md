# Fase 2: Despliegue local del laboratorio

## Objetivo

Levantar el laboratorio local de monitoreo usando Docker Compose.

## Servicios levantados

- PostgreSQL
- Zabbix Server
- Zabbix Web
- Zabbix Agent 2
- Grafana
- Python Flask App
- Nginx demo

## Comandos ejecutados

```bash
cd ~/proyectos/Proyecto-gestion-zabbix
chmod +x scripts/*.sh
./scripts/00_check_prereqs.sh
cp .env.example .env
docker compose config
./scripts/01_start_local_lab.sh
docker compose ps
curl -I http://localhost:8080
curl -I http://localhost:3000
curl http://localhost:5000/health
curl -I http://localhost:8081
