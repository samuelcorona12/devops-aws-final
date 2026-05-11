#!/bin/bash

echo "Creando usuario devops_user..."

sudo useradd devops_user

echo "Asignando permisos..."

sudo mkdir -p /home/devops_user/proyecto

sudo chown -R devops_user:devops_user /home/devops_user/proyecto

echo "Restaurando permisos de Cloud9..."

sudo chown -R ec2-user:ec2-user ~/environment

echo "Proceso completado."

