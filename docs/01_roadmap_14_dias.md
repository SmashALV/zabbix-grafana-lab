# Roadmap de 14 días, 3 horas por día

## Semana 1: base técnica y despliegue local

### Día 1: Linux + Git + objetivo del proyecto

**Meta:** preparar el entorno y entender la arquitectura.

1. Instala Docker, Git y Python.
2. Lee `README.md` y dibuja la arquitectura en papel o draw.io.
3. Crea un repositorio Git.
4. Primer commit: estructura inicial.

**Comandos mínimos:**

```bash
pwd
ls -la
uname -a
ip addr
git init
git status
git add .
git commit -m "Inicio proyecto observabilidad Zabbix Grafana"
```

**Evidencia:** captura de `git log --oneline` y diagrama inicial.

---

### Día 2: Docker Compose y servicios base

**Meta:** levantar el stack local.

```bash
./scripts/00_check_prereqs.sh
cp .env.example .env
./scripts/01_start_local_lab.sh
docker compose ps
```

**Evidencia:** captura de contenedores activos.

---

### Día 3: Zabbix básico

**Meta:** ingresar a Zabbix, reconocer menús y crear hosts.

1. Entra a `http://localhost:8080`.
2. Revisa: Data collection, Hosts, Latest data, Problems.
3. Ejecuta el bootstrap API:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests
python scripts/03_zabbix_api_bootstrap.py
```

**Evidencia:** hosts creados en Zabbix.

---

### Día 4: Métricas Linux y disponibilidad HTTP

**Meta:** observar CPU, memoria, disco y healthchecks.

1. Revisa Latest data del host `LAB - Docker Agent2`.
2. Revisa escenarios web de Flask y Nginx.
3. Genera carga:

```bash
python scripts/04_generate_load.py --requests 30 --cpu-seconds 5
```

**Evidencia:** gráfico de CPU o disponibilidad HTTP.

---

### Día 5: Grafana + datasource Zabbix

**Meta:** conectar Grafana a Zabbix y crear dashboard.

1. Entra a `http://localhost:3000`.
2. Verifica el datasource `Zabbix`.
3. Crea paneles con métricas de Zabbix.
4. Guarda dashboard con nombre: `Portafolio Observabilidad`.

**Evidencia:** captura de dashboard.

---

### Día 6: Networking aplicado

**Meta:** comprender puertos, rutas y servicios.

```bash
ip addr
ip route
ss -tulpn
curl -v http://localhost:5000/health
python scripts/05_network_discovery_scan.py --network 127.0.0.1/32 --ports 3000,5000,8080,8081,10050,10051
```

**Evidencia:** tabla de puertos y explicación de cada puerto.

---

### Día 7: Documentación y primer informe

**Meta:** consolidar semana 1.

1. Actualiza README con tus capturas y problemas encontrados.
2. Ejecuta `scripts/07_export_evidence.sh`.
3. Haz commit.

**Evidencia:** informe corto en Markdown.

---

## Semana 2: cloud, automatización y portafolio

### Día 8: Linux server o VM cloud

**Meta:** practicar una VM Ubuntu real.

1. Crea una VM Ubuntu.
2. Conéctate por SSH.
3. Instala Docker.
4. Clona/sube el proyecto.

**Evidencia:** captura de SSH y `docker --version`.

---

### Día 9: despliegue cloud del stack o agente remoto

**Meta:** desplegar el stack o monitorear una VM externa.

Opción A: ejecutar todo el stack en cloud.  
Opción B: instalar solo Agent2 en la VM y monitorearla desde Zabbix.

```bash
sudo ZBX_SERVER_IP="IP_DEL_ZABBIX" ZBX_HOSTNAME="vm-cloud-01" bash scripts/06_install_agent_ubuntu.sh
```

**Evidencia:** host cloud visible en Zabbix.

---

### Día 10: Ansible opcional

**Meta:** automatizar instalación de agentes.

```bash
cd ansible
cp inventory.ini.example inventory.ini
ansible-playbook -i inventory.ini install-zabbix-agent2.yml
```

**Evidencia:** playbook ejecutado.

---

### Día 11: alertas y problemas

**Meta:** crear al menos 2 condiciones de alerta.

Ideas:

- App Python no responde HTTP 200.
- Nginx no responde.
- CPU alta durante varios minutos.
- Disco usado mayor a cierto porcentaje.

**Evidencia:** captura de Problems.

---

### Día 12: Python + API Zabbix

**Meta:** extender el script Python.

Mejora sugerida:

- Consultar problemas activos.
- Exportar problemas a CSV.
- Mostrar top hosts con más problemas.

**Evidencia:** script y CSV.

---

### Día 13: seguridad mínima y hardening

**Meta:** aplicar buenas prácticas básicas.

1. Cambia contraseñas.
2. Limita puertos expuestos.
3. Crea usuario no root en la VM.
4. Documenta riesgos.

**Evidencia:** checklist de seguridad.

---

### Día 14: entrega final

**Meta:** cerrar portafolio comprobable.

Entrega:

- README final.
- Capturas.
- Dashboard Grafana.
- Evidencia Zabbix.
- Informe de aprendizajes.
- Repositorio Git ordenado.

**Pitch corto:**

> Implementé una infraestructura de observabilidad con Zabbix y Grafana, desplegada con Docker Compose, monitoreando servicios web, métricas de sistema y disponibilidad HTTP. Automatizé el alta inicial mediante Python y documenté evidencias de Linux, networking, cloud y Git.
