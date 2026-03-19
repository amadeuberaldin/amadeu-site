#!/usr/bin/env bash
set -euo pipefail

LOCAL_DIR="$HOME/dev/amadeu-site/frontend/"
REMOTE_USER="amadeu"
REMOTE_HOST="10.10.10.1"
REMOTE_DIR="/var/www/amadeu-site/"

echo "Enviando arquivos para a VPS..."
scp -r "${LOCAL_DIR}"* "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_DIR}"

echo "Deploy concluído."
