import json
import random

def lambda_handler(event, context):

    mensajes = [
        "Microservicio DevOps funcionando correctamente",
        "AWS Lambda ejecutado exitosamente",
        "API Gateway conectado con Lambda",
        "Proyecto DevOps AWS Academy activo",
        "Respuesta generada desde microservicio serverless"
    ]

    return {
        'statusCode': 200,
        'body': json.dumps({
            'mensaje': random.choice(mensajes),
            'servicio': 'microservicio-devops'
        })
    }

