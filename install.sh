#!/bin/bash
set -x
set -e

# Docker files
SERVICE_NAME=lnls-dhcpd-compose.service

# Service files
SERVICE_FILE_DEST=/etc/systemd/system

cp --preserve=mode ${SERVICE_NAME} ${SERVICE_FILE_DEST}

systemctl daemon-reload
systemctl stop ${SERVICE_NAME}
systemctl start ${SERVICE_NAME}

