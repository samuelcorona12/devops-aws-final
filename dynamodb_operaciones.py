import boto3
import time

dynamodb = boto3.resource('dynamodb')

table_name = 'devops-tabla'

# Crear tabla
tabla = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        }
    ],
    BillingMode='PAY_PER_REQUEST'
)

print("Creando tabla...")

tabla.wait_until_exists()

print("Tabla creada")

# Referencia tabla
tabla = dynamodb.Table(table_name)

# Insertar registro
tabla.put_item(
    Item={
        'id': '1',
        'nombre': 'Proyecto DevOps',
        'status': 'activo'
    }
)

print("Registro insertado")

# Actualizar registro
tabla.update_item(
    Key={
        'id': '1'
    },
    UpdateExpression='SET #s = :nuevo',
    ExpressionAttributeNames={
        '#s': 'status'
    },
    ExpressionAttributeValues={
        ':nuevo': 'completado'
    }
)

print("Registro actualizado")

# Eliminar registro
tabla.delete_item(
    Key={
        'id': '1'
    }
)

print("Registro eliminado")
