#!/bin/bash
set -e

NN_DIR="/opt/hadoop/data/nameNode"

echo "Iniciando NameNode"
echo "Directorio de metadatos: $NN_DIR"

if [ ! -d "$NN_DIR/current" ]; then
    echo "No se encuentra un NameNode inicializado. Formateando..."
    hdfs namenode -format -force -nonInteractive
else
    echo "NameNode ya inicializado. Se omite el formateo."
fi

echo "Arrancando servicio NameNode..."
hdfs namenode &

echo "Esperando a que NameNode este listo..."
sleep 10

echo "Arrancando YARN ResourceManager..."
yarn --daemon start resourcemanager

echo "Arrancando YARN NodeManager..."
yarn --daemon start nodemanager

tail -f /dev/null