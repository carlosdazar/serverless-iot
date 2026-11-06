# Monitoreo IoT y Control Bidireccional con ESP32 & AWS

sistema completo de Internet de las Cosas (IoT) basado en arquitectura serverles, permite visualizar en tiempo real datos de temperatura y humedad recolectados por un sensor DHT11 y accionar actuadores (LED) de forma remota mediante un Dashboards web alojado en AWS.

## Integrantes
* Valentina Arciniegas
* Davinson Tulande
* Carlos Daza
* Andres Coral

## 1. Configuración de AWS IoT Core

AWS IoT Core actúa como el *broker* MQTT central que permite la comunicación segura y bidireccional entre el ESP32, las funciones Lambda y el Dashboard Web.

### creación del objeto (Thing)

Un objeto de IoT es una representación digital de su dispositivo físico en la nube, para crear un objeto se realiza le siguiente proceso:

1. Ir a la consola de `AWS IoT core `  > `Administrar ` >`todos los dispositivos ` > `Objetos `


2. Se debe hacer click en la opción `crear objetos ` > `crear un único objeto`

3. En las propiedades del objeto se define el nombre del objeto ej: ` esp32-cocatrace` > siguiente

4. En la parte de certificados, seleccionar `Generar automáticamente un certificado nuevo`> siguiente

5. seleccionar la opción `crear politica`, se despliega una nueva ventana llamada `crear politica`

6. Se asigna un nombre de la política ej `esp32-cocatrace-policy`

7. Se deben asignar los documentos de política, indica de manera estructurada quién puede hacer qué, sobre qué recurso y bajo qué condiciones. En este caso el dispositivo esp32. Se crea lo siguiente

política para otorgar permisos de conexión, publicación y suscripción al ESP32

El uso * es para que estas políticas sirvan en cualquier recurso.

8.  Se crean las políticas > en la pestaña anterior se debe verificar que las políticas estén asociadas al objeto > se crea el objeto.

9. Se generan los certificados y claves, los certificados que se deben descargar son:
    
* **Certificado del dispositivo** (`xxxx-certificate.pem.crt`).
  
* **Clave privada** (`xxxx-private.pem.key`).
  
* **Certificado raíz de Amazon CA1** (`AmazonRootCA1.pem`).

Una vez creado el objeto > dar click al nombre del objeto > certificados > click en el nombre del certificado > políticas 

En caso de no tener políticas adjuntar política > buscar el nombre de la política creada

10. tambien se debe guardar el `end-point` este se ubica en


