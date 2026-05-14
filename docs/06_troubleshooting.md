# Troubleshooting

## Zabbix no carga en localhost:8080

```bash
docker compose ps
docker compose logs -f zabbix-web
docker compose logs -f zabbix-server
```

La primera inicialización puede tardar algunos minutos.

## Error de conexión a PostgreSQL

```bash
docker compose logs postgres
docker compose restart zabbix-server zabbix-web
```

Si estás empezando y no necesitas datos anteriores:

```bash
docker compose down -v
docker compose up -d --build
```

## Grafana no muestra el plugin Zabbix

```bash
docker compose logs grafana | grep -i plugin
```

Revisa que exista:

```yaml
GF_PLUGINS_PREINSTALL: alexanderzobnin-zabbix-app
```

Reinicia:

```bash
docker compose restart grafana
```

## El script API falla por login

Verifica credenciales:

```bash
curl -s http://localhost:8080/api_jsonrpc.php
```

También puedes definir variables:

```bash
export ZBX_USER=Admin
export ZBX_PASSWORD=zabbix
python scripts/03_zabbix_api_bootstrap.py
```

## No aparecen métricas del agente

1. Verifica que el host exista en Zabbix.
2. Verifica DNS: `zabbix-agent2` dentro de Docker.
3. Verifica template Linux.
4. Verifica puerto 10050.

```bash
docker exec -it lab-zabbix-server ping -c 3 zabbix-agent2 || true
docker compose logs zabbix-agent2
```

## Los puertos ya están ocupados

Busca el proceso:

```bash
ss -tulpn | grep -E '3000|5000|8080|8081|10050|10051'
```

Cambia puertos en `docker-compose.yml`.

## En cloud no puedo entrar

Revisa:

- Security Group / firewall cloud.
- UFW de Ubuntu.
- Que Docker esté corriendo.
- Que la app escuche en `0.0.0.0`.
- No usar contraseñas por defecto en Internet.
