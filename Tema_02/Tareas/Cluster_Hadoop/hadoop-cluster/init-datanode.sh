#!/bin/bash
set -e

DN_DIR="/opt/hadoop/data/dataNode"

echo "Iniciando DataNode"
echo "Directorio de datos: $DN_DIR"

if [ -d "$DN_DIR" ]; then
    rm -rf "$DN_DIR"/*
    echo "Directorio datanode borrado correctamente"
else
    echo "El directorio datanode no existe. Creando..."
    mkdir -p "$DN_DIR"
fi

echo "Estableciendo propietario y permisos"
chown -R hadoop:hadoop "$DN_DIR"
chmod 755 "$DN_DIR"

echo "Arrancando servicio DataNode..."
hdfs datanode &

sleep 5

echo "Arrancando YARN NodeManager..."
yarn --daemon start nodemanager

tail -f /dev/null
