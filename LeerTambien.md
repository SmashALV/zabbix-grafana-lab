# Proyecto de autoaprendizaje: Infraestructura de redes y monitoreo de servidores con Zabbix + Grafana

**Resultado esperado para portafolio:** un laboratorio funcional local o cloud donde se monitorean servicios Linux, una aplicación Python, disponibilidad HTTP, consumo de CPU/memoria/disco, eventos de red y visualización en Grafana usando Zabbix como fuente de datos.

---

## 1. Caso a desarrollar

Una pequeña organización académica necesita monitorear una infraestructura mínima compuesta por:

- Un servidor de monitoreo con **Zabbix Server**.
- Una interfaz web de **Zabbix**.
- Una base de datos PostgreSQL para almacenar métricas.
- Un dashboard de **Grafana** conectado a Zabbix.
- Una aplicación web en **Python Flask** que simula un servicio académico.
- Un servidor web **Nginx** como servicio de red básico.
- Un agente **Zabbix Agent 2** para recolectar métricas de sistema.
- Opcionalmente, una VM en la nube para practicar Linux, Git, Docker, firewall y despliegue.

El reto consiste en dejar evidencias de instalación, configuración, monitoreo, alertas, dashboards y automatización.

---

## 2. Arquitectura del laboratorio

```text
Usuario / Navegador
   |
   |-- http://localhost:8080  -> Zabbix Web
   |-- http://localhost:3000  -> Grafana
   |-- http://localhost:5000  -> App Python Flask
   |-- http://localhost:8081  -> Nginx demo

Docker network: monitoring-net
   |
   |-- postgres               -> BD de Zabbix
   |-- zabbix-server          -> Motor de monitoreo
   |-- zabbix-web             -> Frontend Zabbix
   |-- zabbix-agent2          -> Métricas Linux por agente
   |-- grafana                -> Dashboards conectados a Zabbix
   |-- python-app             -> Servicio académico simulado
   |-- sample-nginx           -> Servicio web básico
```

---

## 3. Competencias que vas a practicar

| Área | Qué practicarás | Evidencia sugerida |
|---|---|---|
| Linux | procesos, puertos, servicios, logs, recursos | captura de `htop`, `ss`, `df`, `journalctl` |
| Git | commits, ramas, README, versionado | URL del repositorio o `git log --oneline` |
| Cloud | VM Ubuntu, firewall, SSH, Docker | captura de consola cloud y `docker ps` |
| Automatización | Bash, Python API, Ansible opcional | scripts ejecutados y commit |
| Observabilidad | métricas, triggers, disponibilidad, dashboards | capturas de Zabbix y Grafana |
| Networking | puertos, DNS Docker, HTTP, ICMP, latencia | pruebas `curl`, `ping`, `traceroute`, `ss` |

---

## 4. Requisitos previos

### Opción local

- Windows 10/11 con WSL2 o Linux Ubuntu 22.04/24.04.
- Docker Desktop o Docker Engine.
- Docker Compose v2.
- Git.
- Python 3.10 o superior.
- 6 GB de RAM libres recomendados.

### Opción cloud

Puedes usar AWS, Azure, Google Cloud, Oracle Cloud, DigitalOcean, Linode o similar.

Recomendación mínima para autoaprendizaje:

- Ubuntu 22.04 LTS o 24.04 LTS.
- 2 vCPU.
- 4 GB RAM mínimo; 8 GB mejor.
- 20 GB disco.
- Abrir temporalmente puertos: `22`, `3000`, `5000`, `8080`, `8081`, `10051`.
- No expongas el laboratorio a Internet con contraseñas por defecto.

---

## 5. Estructura del repositorio

```text
.
├── README.md
├── docker-compose.yml
├── .env.example
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── scripts/
│   ├── 00_check_prereqs.sh
│   ├── 01_start_local_lab.sh
│   ├── 02_stop_lab.sh
│   ├── 03_zabbix_api_bootstrap.py
│   ├── 04_generate_load.py
│   ├── 05_network_discovery_scan.py
│   ├── 06_install_agent_ubuntu.sh
│   └── 07_export_evidence.sh
├── grafana/
│   ├── provisioning/
│   │   ├── datasources/zabbix-datasource.yml
│   │   └── dashboards/dashboard-provider.yml
│   └── dashboards/portfolio-dashboard.json
├── ansible/
│   ├── inventory.ini.example
│   └── install-zabbix-agent2.yml
├── cloud/
│   ├── aws-terraform/main.tf
│   ├── aws-terraform/variables.tf
│   └── cloud-init-docker-ubuntu.yml
├── docs/
│   ├── 01_roadmap_14_dias.md
│   ├── 02_comandos_linux_git_networking.md
│   ├── 03_configuracion_zabbix_grafana.md
│   ├── 04_evidencias_portafolio.md
│   ├── 05_rubrica_autoevaluacion.md
│   ├── 06_troubleshooting.md
│   └── 07_recursos_verificados.md
└── evidence/
    └── README.md
```

---

## 6. Despliegue rápido local

### Paso 1: descomprimir y entrar al proyecto

```bash
unzip zabbix-grafana-autoaprendizaje.zip
cd zabbix-grafana-autoaprendizaje
```

### Paso 2: validar prerrequisitos

```bash
chmod +x scripts/*.sh
./scripts/00_check_prereqs.sh
```

### Paso 3: crear archivo `.env`

```bash
cp .env.example .env
```

Puedes dejar los valores por defecto para laboratorio local.

### Paso 4: iniciar el laboratorio

```bash
./scripts/01_start_local_lab.sh
```

Espera 2 a 5 minutos la primera vez porque Zabbix inicializa la base de datos.

### Paso 5: verificar servicios

```bash
docker compose ps
curl -I http://localhost:8080
curl -I http://localhost:3000
curl http://localhost:5000/health
curl -I http://localhost:8081
```

### Paso 6: ingresar a las interfaces

| Servicio | URL | Usuario | Clave |
|---|---|---|---|
| Zabbix | http://localhost:8080 | `Admin` | `zabbix` |
| Grafana | http://localhost:3000 | `admin` | `admin123` |
| App Python | http://localhost:5000 | - | - |
| Nginx | http://localhost:8081 | - | - |

Cambia las contraseñas si lo expones en cloud.

---

## 7. Automatizar alta inicial en Zabbix

Cuando Zabbix ya responda, ejecuta:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests
python scripts/03_zabbix_api_bootstrap.py
```

Este script intenta crear:

- Grupo: `Autoaprendizaje Observabilidad`.
- Host: `LAB - Docker Agent2`.
- Host: `LAB - Python App`.
- Host: `LAB - Nginx`.
- Escenarios web para verificar HTTP 200 en Flask y Nginx.

Si algún template no existe por idioma o versión, el script no se detiene: deja el host creado y te indica qué completar manualmente.

---

## 8. Crear dashboard en Grafana

1. Entra a Grafana: <http://localhost:3000>.
2. Verifica que el datasource **Zabbix** esté creado automáticamente.
3. Si no aparece, crea un datasource manual:
   - Tipo: Zabbix.
   - URL: `http://zabbix-web:8080/api_jsonrpc.php`.
   - Usuario: `Admin`.
   - Password: `zabbix`.
4. Crea un dashboard con paneles:
   - Disponibilidad de `LAB - Python App`.
   - Disponibilidad de `LAB - Nginx`.
   - CPU del host con Agent2.
   - Memoria usada.
   - Disco usado.
   - Problemas activos.

También se incluye un dashboard base en `grafana/dashboards/portfolio-dashboard.json` para documentar el caso y guiar los paneles.

---

## 9. Generar carga para ver métricas

```bash
python scripts/04_generate_load.py --url http://localhost:5000 --requests 60 --cpu-seconds 5
```

Luego revisa:

- Zabbix → Monitoring → Latest data.
- Zabbix → Monitoring → Problems.
- Grafana → Dashboard del proyecto.

---

## 10. Práctica de networking

Ejecuta un descubrimiento simple en tu red local o en la red Docker:

```bash
python scripts/05_network_discovery_scan.py --network 127.0.0.1/32 --ports 3000,5000,8080,8081
```

En Linux también practica:

```bash
ip addr
ip route
ss -tulpn
curl -v http://localhost:5000/health
traceroute 8.8.8.8 || tracepath 8.8.8.8
```

---

## 11. Opción cloud resumida

### Ruta A: subir todo el stack a una VM

1. Crea una VM Ubuntu 22.04/24.04.
2. Instala Docker con `cloud/cloud-init-docker-ubuntu.yml` o manualmente.
3. Sube el ZIP o clona tu repositorio.
4. Ejecuta los mismos pasos del despliegue local.
5. Cambia contraseñas y limita puertos por firewall.

### Ruta B: VM externa monitoreada por Zabbix local/cloud

1. Crea una VM Ubuntu.
2. Instala el agente:

```bash
sudo ZBX_SERVER_IP="IP_DEL_SERVIDOR_ZABBIX" ZBX_HOSTNAME="vm-cloud-01" bash scripts/06_install_agent_ubuntu.sh
```

3. En Zabbix, crea el host `vm-cloud-01` con interfaz Agent puerto `10050`.
4. Asocia template `Linux by Zabbix agent`.
5. Verifica Latest data.

---

## 12. Entregables finales de portafolio

Al finalizar las 2 semanas, debes tener:

1. Repositorio Git con mínimo 10 commits.
2. README propio con decisiones, errores y aprendizajes.
3. Captura de `docker compose ps`.
4. Captura de Zabbix con hosts en verde.
5. Captura de Latest data con CPU, memoria, disco y disponibilidad HTTP.
6. Captura de Grafana con dashboard.
7. Evidencia de script Python consumiendo la API de Zabbix.
8. Evidencia de networking: puertos, rutas, curl, escaneo local controlado.
9. Reporte breve de 2 páginas o Markdown con arquitectura, problemas encontrados y mejoras futuras.

Para exportar evidencias automáticas básicas:

```bash
./scripts/07_export_evidence.sh
```

---

## 13. Cierre del proyecto

Cuando termines, apaga el laboratorio:

```bash
./scripts/02_stop_lab.sh
```

Si quieres borrar volúmenes y empezar de cero:

```bash
docker compose down -v
```

---

## 14. Validación de networking y diagnóstico

Se realizaron pruebas de conectividad para validar la comunicación entre servicios del laboratorio:

- Identificación de puertos publicados con `ss -tulpn`.
- Revisión de interfaces y rutas con `ip addr` e `ip route`.
- Inspección de la red Docker creada por Compose.
- Pruebas HTTP con `curl -v`.
- Validación de comunicación interna entre contenedores usando nombres de servicio Docker.
- Escaneo local controlado con `scripts/05_network_discovery_scan.py`.

Los resultados fueron documentados en la carpeta `evidence/`.

## 15. Siguientes mejoras

- Agregar alertas por correo o Telegram.
- Monitorear una VM real en cloud.
- Agregar SNMP para simular monitoreo de red.
- Usar Ansible para instalar agentes en varias máquinas.
- Publicar el dashboard y capturas en un informe académico.
- Crear una pequeña API en Python que consulte problemas activos en Zabbix y genere un reporte CSV.