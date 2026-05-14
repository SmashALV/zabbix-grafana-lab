#!/usr/bin/env bash
set -euo pipefail

# Instalación básica de Zabbix Agent 2 en Ubuntu 22.04/24.04 para VM local o cloud.
# Uso:
#   sudo ZBX_SERVER_IP="IP_DEL_ZABBIX" ZBX_HOSTNAME="vm-cloud-01" bash scripts/06_install_agent_ubuntu.sh

ZBX_SERVER_IP="${ZBX_SERVER_IP:-127.0.0.1}"
ZBX_HOSTNAME="${ZBX_HOSTNAME:-$(hostname)}"
UBUNTU_VERSION="${UBUNTU_VERSION:-$(. /etc/os-release && echo ${VERSION_ID})}"

case "$UBUNTU_VERSION" in
  22.04) ZBX_UBUNTU="ubuntu22.04" ;;
  24.04) ZBX_UBUNTU="ubuntu24.04" ;;
  *) echo "Versión Ubuntu no validada automáticamente: $UBUNTU_VERSION. Usa 22.04 o 24.04."; exit 1 ;;
esac

echo "Instalando Zabbix Agent 2 para Ubuntu $UBUNTU_VERSION"
apt-get update
apt-get install -y wget gnupg lsb-release ca-certificates
wget -O /tmp/zabbix-release.deb "https://repo.zabbix.com/zabbix/7.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_latest_7.0+${ZBX_UBUNTU}_all.deb"
dpkg -i /tmp/zabbix-release.deb
apt-get update
apt-get install -y zabbix-agent2

sed -i "s/^Server=.*/Server=${ZBX_SERVER_IP}/" /etc/zabbix/zabbix_agent2.conf
sed -i "s/^ServerActive=.*/ServerActive=${ZBX_SERVER_IP}/" /etc/zabbix/zabbix_agent2.conf
sed -i "s/^Hostname=.*/Hostname=${ZBX_HOSTNAME}/" /etc/zabbix/zabbix_agent2.conf

systemctl enable zabbix-agent2
systemctl restart zabbix-agent2
systemctl status zabbix-agent2 --no-pager

echo "Listo. Crea el host '${ZBX_HOSTNAME}' en Zabbix con IP de esta VM y puerto 10050."
