# Comandos esenciales de Linux, Git y Networking

## Linux básico

```bash
pwd
ls -lah
cd /ruta
mkdir evidencia
touch evidencia/notas.txt
cat /etc/os-release
uname -a
whoami
id
```

## Procesos y servicios

```bash
ps aux | head
ps aux | grep zabbix
top
htop
systemctl status docker
journalctl -u docker --no-pager -n 50
```

## Disco y memoria

```bash
df -h
free -h
du -sh *
```

## Red

```bash
ip addr
ip route
ss -tulpn
ping -c 4 8.8.8.8
curl -I http://localhost:8080
curl -v http://localhost:5000/health
```

## Docker

```bash
docker version
docker compose version
docker compose ps
docker compose logs -f zabbix-server
docker exec -it lab-zabbix-server sh
docker inspect lab-python-app
```

## Git

```bash
git init
git status
git add .
git commit -m "mensaje claro"
git log --oneline --graph --decorate
git checkout -b feature/dashboard
git diff
```

## Diagnóstico de puertos

```bash
ss -tulpn | grep -E '3000|5000|8080|8081|10050|10051'
curl -I http://localhost:3000
curl -I http://localhost:8080
```

## Firewall básico Ubuntu

```bash
sudo ufw status
sudo ufw allow OpenSSH
sudo ufw allow from TU_IP_PUBLICA to any port 3000 proto tcp
sudo ufw allow from TU_IP_PUBLICA to any port 8080 proto tcp
sudo ufw enable
```
