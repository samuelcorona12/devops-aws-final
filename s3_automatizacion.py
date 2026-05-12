import boto3
from datetime import datetime

s3 = boto3.client('s3')

bucket_name = 'devops-stack-devopsbucket-vfoyqvco4wne'

# Crear archivo local
archivo = 'archivo_prueba.txt'

with open(archivo, 'w') as f:
    f.write('Archivo generado automaticamente para DevOps AWS\n')

print("Archivo local creado")

# Subir archivo
s3.upload_file(archivo, bucket_name, f'pruebas/{archivo}')

print("Archivo subido a S3")

# Listar objetos
respuesta = s3.list_objects_v2(Bucket=bucket_name)

print("\nObjetos en bucket:\n")

if 'Contents' in respuesta:
    for obj in respuesta['Contents']:
        print(f"Nombre: {obj['Key']}")
        print(f"Tamaño: {obj['Size']} bytes")
        print(f"Última modificación: {obj['LastModified']}")
        print("---------------------------")
else:
    print("Bucket vacío")
