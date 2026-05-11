#!/bin/bash

echo "Actualizando sistema..."
sudo yum update -y

echo "Instalando dependencias..."
sudo yum install -y git python3 docker

echo "Instalando boto3..."
pip3 install boto3

echo "Iniciando Docker..."
sudo service docker start

echo "Configuración completada."
