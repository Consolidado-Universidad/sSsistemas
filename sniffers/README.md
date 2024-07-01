## Sniffing

### ¿Que es sniffing?

Es una técnica que permite capturar y analizar los paquetes de información que circulan por una red. El objetivo de esta técnica es obtener información sensible de los usuarios de la red, como contraseñas, correos electrónicos, números de tarjetas de crédito, etc.

Pueden capturar cualquier tipo de información que circule por la red, como correos electrónicos, contraseñas, números de tarjetas de crédito, etc.

### Usuos NO maliciosos de los sniffers

1. Administracion y gestion de informacion que cirule a través de una red LAN 
2. Auditoria de seguridad
3. Identificar estabilidad y vulnerabilidades de la red LAN
4. Verificar el tráfico de la red y monitorear el rendimiento de la red
5. Prevenir actividades de espionaje y sabotaje
6. Monitorear las actividades de los usuarios de la red
7. Identificar paquetes de datos

## Herramientas de sniffing

### Wireshark

Wireshark es una herramienta de software libre que permite analizar el tráfico de una red en tiempo real. Es una herramienta muy potente y versátil que permite capturar y analizar paquetes de datos en tiempo real.

**Analisis de Ethernet Controller**: Un controlador Ethernet es un dispositivo de hardware que se utiliza para conectar una computadora a una red Ethernet. El controlador Ethernet se encarga de enviar y recibir paquetes de datos a través de la red Ethernet. Wireshark permite analizar el tráfico de un controlador Ethernet y mostrar información detallada sobre los paquetes de datos que se envían y reciben a través de la red Ethernet.

## Mitigar ataques de sniffing

1. Recursos de hardware: 
2. Segmentacion de la red mediante el uso de switch: Permite no exhibir la totalidad de la red a los atacantes, sino solamente la parte de la red a la que se conectan.
3. Recursos de sotware:
    * Cripotgrafia: Permite cifrar la información que se envía a través de la red, de modo que los atacantes no puedan leerla.
    * VPN: Permite crear una red privada virtual que cifra la información que se envía a través de la red, de modo que los atacantes no puedan leerla.
    * Evitar Webs sin HTTPS: Evitar navegar por sitios web que no utilizan HTTPS, ya que la información que se envía a través de estos sitios web no está cifrada y puede ser capturada por los atacantes.
    * Autebticacion: Utilizar mecanismos de autenticación fuertes, como contraseñas seguras, autenticación de dos factores, etc.