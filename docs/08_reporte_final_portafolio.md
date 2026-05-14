# Reporte final del proyecto: Infraestructura de monitoreo con Zabbix y Grafana

## 1. Resumen ejecutivo

Se implementó un laboratorio local de observabilidad usando Docker Compose, Zabbix, Grafana, PostgreSQL, Zabbix Agent 2, una aplicación Python Flask y un servicio Nginx. El objetivo fue simular una infraestructura mínima de una organización académica y monitorear disponibilidad HTTP, métricas de sistema, eventos, problemas activos y recuperación ante fallos.

El proyecto permitió practicar administración básica de Linux, contenedores Docker, monitoreo con Zabbix, visualización con Grafana, automatización con Python API, diagnóstico de red y documentación técnica orientada a portafolio.

## 2. Arquitectura implementada

El laboratorio se compone de los siguientes servicios:

| Componente | Función |
|---|---|
| PostgreSQL | Base de datos para almacenar métricas de Zabbix |
| Zabbix Server | Motor de monitoreo y procesamiento de eventos |
| Zabbix Web | Interfaz web para gestión de hosts, triggers y problemas |
| Zabbix Agent 2 | Recolección de métricas del sistema |
| Grafana | Visualización de métricas y problemas |
| Python Flask App | Servicio académico simulado |
| Nginx | Servicio web básico monitoreado |
| Docker Compose | Orquestación local de servicios |

## 3. Herramientas utilizadas

- Windows 10/11
- WSL2 con Ubuntu 22.04
- Docker Desktop
- Docker Compose v2
- Git y GitHub
- Python 3
- Zabbix
- Grafana
- PostgreSQL
- Nginx
- Flask
- Bash
- curl, ss, ip, tracepath

## 4. Fases desarrolladas

### Fase 1: Preparación del entorno

Se configuró WSL2 con Ubuntu 22.04, Docker Desktop, Git, Python y Visual Studio Code conectado a WSL.

### Fase 2: Despliegue local

Se levantaron los servicios del laboratorio con Docker Compose y se validó el acceso a Zabbix, Grafana, Flask y Nginx.

### Fase 3: Automatización con Zabbix API

Se ejecutó un script Python para crear grupo de hosts, hosts monitoreados y escenarios web para validar disponibilidad HTTP.

### Fase 4: Dashboard en Grafana

Se configuró Grafana con Zabbix como datasource y se construyó un dashboard con disponibilidad HTTP, CPU, memoria, disco y problemas activos.

### Fase 5: Fallos controlados

Se detuvieron servicios de forma controlada para generar problemas en Zabbix y validar su visualización en Grafana. Luego se restauraron los servicios para evidenciar recuperación.

### Fase 6: Networking y diagnóstico

Se validaron puertos, rutas, red Docker, comunicación interna entre contenedores, pruebas HTTP y escaneo local controlado.

### Fase 7: Documentación final

Se consolidaron evidencias, capturas, comandos, aprendizajes y mejoras futuras en un reporte técnico y README profesional.

## 5. Pruebas realizadas

| Prueba | Herramienta | Resultado |
|---|---|---|
| Estado de contenedores | docker compose ps | Servicios activos |
| Validación HTTP | curl | Servicios accesibles |
| Automatización Zabbix | Python requests | Hosts y escenarios creados |
| Dashboard | Grafana | Métricas visualizadas |
| Fallo Nginx | docker compose stop | Problema detectado |
| Fallo Flask | docker compose stop | Problema detectado |
| Recuperación | docker compose start | Problemas resueltos |
| Puertos | ss -tulpn | Puertos identificados |
| Escaneo local | Python script | Puertos abiertos detectados |

## 6. Problemas encontrados y soluciones

| Problema | Causa probable | Solución aplicada |
|---|---|---|
| Grafana no mostraba métricas | Datasource o plugin pendiente | Verificación del datasource Zabbix |
| La carga no generaba problemas | Los endpoints respondían correctamente | Se crearon triggers y fallos controlados |
| Algunas métricas tardaban en aparecer | Intervalos de recolección de Zabbix | Esperar ciclos de monitoreo |
| Servicios no respondían tras reinicio | Contenedor detenido | Validación con docker compose ps y reinicio |

## 7. Evidencias principales

Las evidencias se encuentran en la carpeta `evidence/` e incluyen:

- Estado de contenedores.
- Salidas de curl.
- Salida del script de Zabbix API.
- Capturas de Zabbix Hosts.
- Capturas de Latest Data.
- Capturas de Grafana Dashboard.
- Evidencias de fallos controlados.
- Evidencias de networking y diagnóstico.

## 8. Aprendizajes obtenidos

- Uso de Docker Compose para levantar una infraestructura de monitoreo.
- Configuración inicial de Zabbix y Grafana.
- Automatización de objetos de monitoreo mediante Python API.
- Creación de dashboards de observabilidad.
- Diagnóstico de servicios mediante logs, puertos y conectividad.
- Validación de fallos y recuperación de servicios.
- Documentación técnica para portafolio profesional.

## 9. Mejoras futuras

- Agregar alertas por Telegram o correo.
- Monitorear una VM real en cloud.
- Instalar Zabbix Agent 2 en servidores externos.
- Agregar Ansible para automatizar agentes.
- Exportar problemas activos a CSV mediante una API Python.
- Añadir SNMP para simular monitoreo de red.
- Crear un despliegue cloud en Azure, AWS u Oracle Cloud.

## 10. Conclusión

El proyecto permitió construir un laboratorio funcional de observabilidad integrando monitoreo, visualización, automatización, diagnóstico de red y documentación técnica. La solución demuestra competencias prácticas en Linux, Docker, Zabbix, Grafana, Python, networking y troubleshooting, aplicables a roles iniciales de infraestructura, soporte, DevOps, monitoreo, automatización o transformación digital.
