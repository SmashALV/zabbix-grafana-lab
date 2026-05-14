# Evidencias del proyecto

Esta carpeta contiene evidencias técnicas del laboratorio de monitoreo con Zabbix, Grafana, Docker, Flask y Nginx.

## Fase 2: Despliegue local

- Estado de contenedores con `docker compose ps`.
- Validación HTTP de Zabbix, Grafana, Flask y Nginx.

## Fase 3: Automatización con Zabbix API

- Ejecución del script `03_zabbix_api_bootstrap.py`.
- Creación de grupo de hosts.
- Creación de hosts monitoreados.
- Creación de escenarios web.

## Fase 4: Dashboard en Grafana

- Datasource Zabbix en Grafana.
- Dashboard de disponibilidad HTTP.
- Paneles de CPU, memoria, disco y problemas activos.

## Fase 5: Fallos controlados

- Detención controlada de Nginx.
- Detección del problema en Zabbix.
- Visualización del problema en Grafana.
- Recuperación del servicio.
- Detención y recuperación de Python Flask App.

## Fase 6: Networking y diagnóstico

- Puertos abiertos con `ss -tulpn`.
- Interfaces y rutas con `ip addr` e `ip route`.
- Escaneo local controlado con Python.
- Pruebas HTTP con `curl -v`.
- Comunicación interna entre contenedores.

## Fase 7: Consolidación final

- Estado final del laboratorio.
- Reporte técnico.
- README profesional actualizado.