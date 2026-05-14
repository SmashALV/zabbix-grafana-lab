# Infraestructura de monitoreo con Zabbix + Grafana

Proyecto de portafolio orientado a la implementación de un laboratorio local de observabilidad usando Zabbix, Grafana, Docker, PostgreSQL, Nginx y una aplicación Python Flask.

## Objetivo

Implementar un entorno de monitoreo para validar disponibilidad HTTP, métricas de sistema, eventos, problemas activos, generación de carga, fallos controlados y recuperación de servicios.

## Arquitectura

```text
Usuario / Navegador
   |
   |-- http://localhost:8080  -> Zabbix Web
   |-- http://localhost:3000  -> Grafana
   |-- http://localhost:5000  -> Python Flask App
   |-- http://localhost:8081  -> Nginx demo

Docker network
   |
   |-- postgres
   |-- zabbix-server
   |-- zabbix-web
   |-- zabbix-agent2
   |-- grafana
   |-- python-app
   |-- sample-nginx
Tecnologías utilizadas
Docker
Docker Compose
Zabbix Server
Zabbix Agent 2
Zabbix Web
Grafana
PostgreSQL
Python
Flask
Nginx
Bash
Linux / WSL2 Ubuntu 22.04
Git y GitHub
Funcionalidades implementadas
Despliegue local de laboratorio con Docker Compose.
Monitoreo de disponibilidad HTTP para Flask y Nginx.
Recolección de métricas de CPU, memoria y disco.
Dashboard en Grafana conectado a Zabbix.
Automatización de hosts y escenarios web mediante Python y Zabbix API.
Pruebas de carga sobre servicio Flask.
Fallos controlados y validación de recuperación.
Diagnóstico de red con curl, ss, ip route, Docker networks y escaneo local controlado.
Documentación de evidencias para portafolio.
Requisitos
Windows 10/11 con WSL2 o Linux Ubuntu 22.04/24.04.
Docker Desktop o Docker Engine.
Docker Compose v2.
Git.
Python 3.10 o superior.
Ejecución local
chmod +x scripts/*.sh
cp .env.example .env
./scripts/01_start_local_lab.sh

Verificar servicios:

docker compose ps
curl -I http://localhost:8080
curl -I http://localhost:3000
curl http://localhost:5000/health
curl -I http://localhost:8081
Accesos locales
Servicio	URL	Usuario	Clave
Zabbix	http://localhost:8080
	Admin	zabbix
Grafana	http://localhost:3000
	admin	admin123
Flask App	http://localhost:5000
	-	-
Nginx	http://localhost:8081
	-	-

Nota: las credenciales por defecto solo deben usarse en laboratorio local. Para cloud o exposición externa deben cambiarse.

Automatización con Zabbix API
python3 -m venv .venv
source .venv/bin/activate
pip install requests
python scripts/03_zabbix_api_bootstrap.py

El script crea:

Grupo de monitoreo.
Host para Zabbix Agent 2.
Host para Python Flask App.
Host para Nginx.
Escenarios web HTTP.
Generación de carga
python scripts/04_generate_load.py --url http://localhost:5000 --requests 60 --cpu-seconds 5
Diagnóstico de networking
ip addr
ip route
ss -tulpn
curl -v http://localhost:5000/health
python scripts/05_network_discovery_scan.py --network 127.0.0.1/32 --ports 3000,5000,8080,8081
Fallos controlados

Detener Nginx:

docker compose stop sample-nginx

Restaurar Nginx:

docker compose start sample-nginx

Detener Flask:

docker compose stop python-app

Restaurar Flask:

docker compose start python-app
Evidencias

Las evidencias se encuentran en la carpeta evidence/.

Incluyen:

Estado de contenedores.
Validaciones HTTP.
Automatización con API de Zabbix.
Dashboard en Grafana.
Fallos controlados.
Recuperación de servicios.
Diagnóstico de red.
Logs de servicios.
Reporte final

El reporte completo se encuentra en:

docs/08_reporte_final_portafolio.md

## Mejoras futuras

- Configurar alertas por Telegram o correo.
- Monitorear una VM Ubuntu externa con Zabbix Agent 2.
- Automatizar instalación de agentes con Ansible.
- Agregar métricas de red mediante SNMP.
- Publicar una versión cloud del laboratorio.
- Crear una API Python para consultar problemas activos y exportarlos a CSV.
- Integrar reportes automáticos de disponibilidad.

José Bustillos
Estudiante de Ingeniería de Sistemas
GitHub: https://github.com/SmashALV