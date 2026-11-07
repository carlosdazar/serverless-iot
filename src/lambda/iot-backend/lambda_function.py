import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('valores-sensor-dht11')

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    try:
        # Escanear todos los registros de la tabla
        response = table.scan()
        items = response.get('Items', [])
        
        # Ordenar de más NUEVO a más VIEJO según el timestamp (como número)
        items_ordenados = sorted(
            items, 
            key=lambda x: int(x.get('timestamp', 0)), 
            reverse=True
        )
        
        # Tomar solo los últimos 50 registros más recientes
        ultimos_registros = items_ordenados[:50]
        
        # Invertir la lista para enviarlos en orden cronológico correcto a la gráfica
        ultimos_registros.reverse()
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(ultimos_registros, cls=DecimalEncoder)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }