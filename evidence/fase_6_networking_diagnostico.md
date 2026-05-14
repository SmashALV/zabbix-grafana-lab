# Fase 6: Networking, puertos y diagnóstico Linux

## Objetivo

Validar la conectividad del laboratorio de monitoreo, identificando puertos expuestos, redes Docker, rutas, resolución DNS interna entre contenedores y disponibilidad HTTP de los servicios.

## Servicios analizados

| Servicio | Puerto local | Función |
|---|---:|---|
| Zabbix Web | 8080 | Interfaz de monitoreo |
| Grafana | 3000 | Dashboard de observabilidad |
| Python Flask App | 5000 | Servicio académico simulado |
| Nginx demo | 8081 | Servicio web básico |
| Zabbix Server | 10051 | Motor de monitoreo |
| Zabbix Agent 2 | 10050 | Recolección de métricas |

## Comandos principales usados

```bash
docker compose ps
docker compose ps --services
docker network ls
docker network inspect NOMBRE_DE_LA_RED
ss -tulpn
ip addr
ip route
curl -v http://localhost:5000/health
curl -v http://localhost:8081
docker compose exec zabbix-server wget -qO- http://python-app:5000/health
docker compose exec zabbix-server wget -qO- http://sample-nginx:80
python scripts/05_network_discovery_scan.py --network 127.0.0.1/32 --ports 3000,5000,8080,8081
tracepath 8.8.8.8
