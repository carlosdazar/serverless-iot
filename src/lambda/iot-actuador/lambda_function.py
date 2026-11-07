import json
import boto3

# Instanciar el cliente de AWS IoT Data
iot_client = boto3.client('iot-data', region_name='us-east-1')

def lambda_handler(event, context):
    try:
        # Leer el cuerpo de la petición enviada desde la web
        body = json.loads(event.get('body', '{}')) if isinstance(event.get('body'), str) else event.get('body', {})
        
        # Extraer el estado ON u OFF y el dispositivo
        estado = body.get('estado', 'OFF')
        device_id = body.get('device_id', 'ESP32')
        
        # Construir el mensaje a enviar
        mensaje = {
            "device_id": device_id,
            "message": estado,
            "timestamp": str(event.get('requestContext', {}).get('requestTimeEpoch', ''))
        }
        
        # Topic MQTT que escucha el ESP32
        topico_mqtt = "esp32/actuadores"
        
        iot_client.publish(
            topic=topico_mqtt,
            qos=1,
            payload=json.dumps(mensaje)
        )
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Methods': 'POST,OPTIONS'
            },
            'body': json.dumps({'mensaje': f'Comando {estado} enviado exitosamente al topico {topico_mqtt}'})
        }
        
    except Exception as e:
        print("Error al publicar en IoT Core:", str(e))
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Methods': 'POST,OPTIONS'
            },
            'body': json.dumps({'error': str(e)})
        }