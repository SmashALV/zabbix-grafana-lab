# Fase 4: Dashboard en Grafana conectado a Zabbix

## Objetivo

Configurar Grafana como herramienta de visualización conectada a Zabbix y construir un dashboard de observabilidad para servicios y recursos del laboratorio.

## Servicios visualizados

- LAB - Docker Agent2
- LAB - Python App
- LAB - Nginx

## Datasource usado

- Nombre: Zabbix
- Tipo: Zabbix
- URL interna Docker: http://zabbix-web:8080/api_jsonrpc.php
- Usuario: Admin

## Paneles creados

| Panel | Host | Tipo de visualización | Métrica |
|---|---|---|---|
| Python App - HTTP Status | LAB - Python App | Stat | Código HTTP / escenario web |
| Nginx - HTTP Status | LAB - Nginx | Stat | Código HTTP / escenario web |
| CPU utilization | LAB - Docker Agent2 | Time series | CPU |
| Memory usage | LAB - Docker Agent2 | Gauge / Time series | Memoria |
| Disk usage | LAB - Docker Agent2 | Gauge / Time series | Disco |
| Zabbix - Problemas activos | Grupo completo | Table | Problems |

## Validaciones realizadas

```bash
docker compose ps
curl -I http://localhost:3000
curl -I http://localhost:8080
python scripts/04_generate_load.py --url http://localhost:5000 --requests 60 --cpu-seconds 5
