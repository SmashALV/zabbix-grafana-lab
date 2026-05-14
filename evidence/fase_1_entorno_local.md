# Fase 1: Preparación del entorno local

## Entorno usado

- Sistema operativo host: Windows 10/11
- Subsistema Linux: WSL2
- Distribución: Ubuntu 22.04 LTS
- Editor: Visual Studio Code con extensión WSL
- Contenedores: Docker Desktop con integración WSL2
- Lenguaje auxiliar: Python 3
- Control de versiones: Git + GitHub

## Validaciones realizadas

```bash
lsb_release -a
docker --version
docker compose version
git --version
python3 --version
./scripts/00_check_prereqs.sh