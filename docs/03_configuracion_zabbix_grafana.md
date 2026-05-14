# Configuración de Zabbix y Grafana

## Zabbix: primeros pasos

1. Entra a `http://localhost:8080`.
2. Usuario: `Admin`.
3. Clave: `zabbix`.
4. Cambia la clave si desplegaste en cloud.

## Crear grupo de hosts

Ruta: **Data collection → Host groups → Create host group**.

Nombre sugerido:

```text
Autoaprendizaje Observabilidad
```

## Crear host con Agent2

Ruta: **Data collection → Hosts → Create host**.

- Host name: `LAB - Docker Agent2`.
- Group: `Autoaprendizaje Observabilidad`.
- Interface: Agent.
- DNS name: `zabbix-agent2`.
- Port: `10050`.
- Template: `Linux by Zabbix agent`.

## Crear escenario web para Flask

Ruta: **Data collection → Hosts → LAB - Python App → Web scenarios**.

- Name: `Python App Healthcheck`.
- Step name: `GET health`.
- URL: `http://python-app:5000/health`.
- Required status codes: `200`.

## Crear escenario web para Nginx

- Name: `Nginx Healthcheck`.
- URL: `http://sample-nginx:80/`.
- Required status codes: `200`.

## Grafana: conectar datasource Zabbix

El proyecto intenta provisionarlo automáticamente. Si necesitas hacerlo manualmente:

1. Grafana → Connections → Data sources.
2. Add data source.
3. Selecciona Zabbix.
4. URL: `http://zabbix-web:8080/api_jsonrpc.php`.
5. Username: `Admin`.
6. Password: `zabbix`.
7. Save & test.

## Paneles mínimos del dashboard

- CPU utilization.
- Memory available.
- Disk usage.
- Python App HTTP status.
- Nginx HTTP status.
- Problems activos.

## Alertas mínimas sugeridas

- Servicio Python no responde.
- Servicio Nginx no responde.
- CPU mayor a 80% por varios minutos.
- Disco usado mayor a 80%.

## Nota sobre nombres de templates

Los nombres de templates pueden variar por versión, idioma o importación. Si el script no encuentra `Linux by Zabbix agent`, créalo manualmente desde la interfaz usando el template Linux disponible.
