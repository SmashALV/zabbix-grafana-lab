# Evidencias para portafolio

Crea una carpeta `evidence/` y guarda capturas con nombres claros.

## Evidencias obligatorias

| Evidencia | Archivo sugerido | Descripción |
|---|---|---|
| Docker activo | `01-docker-compose-ps.png` | Contenedores levantados |
| Zabbix login | `02-zabbix-home.png` | Ingreso exitoso |
| Hosts monitoreados | `03-zabbix-hosts.png` | Hosts creados y visibles |
| Latest data | `04-latest-data.png` | Métricas CPU/memoria/disco/HTTP |
| Problems | `05-problems.png` | Alerta simulada o problema resuelto |
| Grafana datasource | `06-grafana-datasource.png` | Zabbix conectado |
| Grafana dashboard | `07-grafana-dashboard.png` | Paneles operativos |
| Git log | `08-git-log.png` | Historial de commits |
| Networking | `09-networking-ports.png` | `ss`, `curl`, escaneo local |
| Cloud opcional | `10-cloud-vm.png` | VM o agente remoto |

## Plantilla de mini informe

```markdown
# Informe de laboratorio: Zabbix + Grafana

## 1. Objetivo
Implementar un laboratorio de observabilidad para monitorear servidores y servicios web usando Zabbix y Grafana.

## 2. Arquitectura
Describir componentes, puertos y flujo de monitoreo.

## 3. Implementación
Explicar Docker Compose, aplicación Python, Zabbix Agent2 y Grafana.

## 4. Evidencias
Insertar capturas y breve explicación.

## 5. Problemas encontrados
Registrar errores, causa y solución.

## 6. Aprendizajes
Linux, Git, cloud, automatización, observabilidad y networking.

## 7. Mejoras futuras
Alertas, SNMP, Ansible, cloud, seguridad.
```
