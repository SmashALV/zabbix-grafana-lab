# Fase 5: Fallos controlados y validación de problemas

## Objetivo

Provocar fallos controlados en servicios monitoreados para validar la detección de problemas en Zabbix y su visualización en Grafana.

## Servicios evaluados

- LAB - Nginx
- LAB - Python App

## Triggers creados

| Host | Trigger | Expresión |
|---|---|---|
| LAB - Nginx | Nginx - Healthcheck HTTP fallando | `last(/LAB - Nginx/web.test.fail[Nginx Healthcheck])<>0` |
| LAB - Python App | Python App - Healthcheck HTTP fallando | `last(/LAB - Python App/web.test.fail[Python App Healthcheck])<>0` |

## Fallo 1: Nginx detenido

Comando usado:

```bash
docker compose stop sample-nginx
