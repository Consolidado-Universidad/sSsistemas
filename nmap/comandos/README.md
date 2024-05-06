## Descubrimiento de hosts

| Flag        | Descripción            |
| ----------- | ---------------------- |
| -sP         | Sondeo ping            |
| -PS         | TCP SYN ping           |
| -PA         | TCP ACK ping           |
| -PU         | UDP ping               |
| -PY         | SCTP Init ping         |
| -PE         | ICMP echo ping         |
| -PP         | ICMP Timestamp ping    |
| -PM         | ICMP address mask ping |
| -PO         | IP protocol ping       |
| -PR         | ARP ping               |
| -traceroute | Hace un traceroute     |
| -P0         | No realiza ping        |
| -sL         | Sondeo de lista        |

## Analisis de puertos
| Flag | Descripción                                                                                                                                                                |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -sT  | Inicia conexiones completas. Muy fácil de detectar                                                                                                                         |
| -sS  | Envía un TCP SYN y espera la respuesta. Si el puerto está abierto se recibe un SYN-ACK y envía un RSP para cerrar la conexión. Si está cerrado recibe un RST               |
| -sF  | Envía un paquete vacío con FIN                                                                                                                                             |
| -sX  | Ataque XMAS. Activa los flags FIN, URG Y PUSH                                                                                                                              |
| -sN  | No activa ningún flag de la cabecera TCP                                                                                                                                   |
| -sP  | Utilizado en descubrimiento de Sistemas. Envía un ICMP y un TCP SYN al puerto 80                                                                                           |
| -sU  | Se envía una cabecera UDP a cada puerto objetivo. Si se recibe error ICMP el puerto está cerrado, si se recibe el error ICMP "no alcanzable" el puerto está filtrado       |
| -sT  | Envía un TCP ACK y se espera un RST                                                                                                                                        |
| -sS  | Envía un TCP SYN y se espera un RST                                                                                                                                        |
| -sI  | Se utilizan paquetes ICMP                                                                                                                                                  |
| -sW  | Se utilizan barridos "-PI" y "-PT" en paralelo                                                                                                                             |
| -sW  | Igual que "-PT" pero se aprovecha de un detalle de implementación que permite listar puertos abiertos en vez de no filtrados cuando se envía un TCP ACK y se espera un RST |


## Ver Paquetes recibidos y enviados por Nmap
```bash	
nmap -sS [IP] -p [Puerto], [Puerto], [Puerto] --packet-trace
```


## Analisis de servicios
| Flag             | Descripción                                                                                                   |
| ---------------- | ------------------------------------------------------------------------------------------------------------- |
| `-sV`            | Detección de las versiones de los servicios                                                                   |
| `--all-ports`    | Escanea todos los puertos                                                                                     |
| `-O`             | Descubrimiento de la versión del S.O.                                                                         |
| `--osscan-guess` | Intenta adivinar S.O. por aproximación                                                                        |
| `-sR`            | Se envían ordenes de programa NULL SunRPC a todos los puertos para determinar si son puertos RPC y su versión |


## Formato de salida
| Flag            | Descripción                  |
| --------------- | ---------------------------- |
| `-oN <fichero>` | Redirige la salida normal    |
| `-oX <fichero>` | Salida en XML                |
| `-oS <fichero>` | Salida «script kiddie»       |
| `-oG <fichero>` | Salida «grepable»            |
| `-oA <fichero>` | Salida en todos los formatos |

## Evasion
| Flag           | Descripción                                                                  |
| -------------- | ---------------------------------------------------------------------------- |
| `-f`           | Fragmenta los paquetes                                                       |
| `--mtu <TAM>`  | Se especifica un tamaño MTU concreto                                         |
| `-S <ip>`      | Se falsea la dirección origen                                                |
| `-sl <zombie>` | Se utiliza como origen una máquina inactiva, haciéndola parecer el emisor    |
| `-D <señuelo>` | Se utilizan equipos señuelo para simular múltiples IPs de origen del escaneo |
| `-g <puerto>`  | Se falsea el puerto de origen                                                |


## nmap scripting engine
| Flag                                     | Descripción                          |
| ---------------------------------------- | ------------------------------------ |
| `-sC`                                    | Ejecuta los scripts por defecto      |
| `--script=<ScriptName>\<ScriptCategory>` | Ejecuta uno o más scripts            |
| `--script-args=<Name1=Value1,...>`       | Usa la lista de argumentos de script |
| `--script-updatedb`                      | Actualiza la base de datos de script |

## Categorias de scripts
| Categoría | Descripción                                                                                                                                  |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| auth      | ejecuta todos sus scripts disponibles para autenticación                                                                                     |
| broadcast | Descubra hosts no incluidos en la línea de comando transmitiendo en la red local                                                             |
| brute     | Intente adivinar las contraseñas en los sistemas objetivo, para una variedad de protocolos                                                   |
| default   | Scripts que se ejecutan por defecto al poner los flags -sC o -A                                                                              |
| discovery | Intenta obtener más información sobre los hosts de destino a través de fuentes públicas de información, SNMP, servicios de directorio y más. |
| dos       | Puede causar condiciones de denegación de servicio en los hosts objetivos.                                                                   |
| exploit   | Intenta explotar los sistemas objetivos                                                                                                      |
| external  | Interactuar con sistemas de terceros no incluidos en la lista de objetivos                                                                   |
| fuzzer    | Envía entradas inesperadas a los campos de los protocolo de red.                                                                             |
| intrusive | Puede bloquear el objetivo, consumir recursos excesivos o afectar de manera maliciosa las máquinas.                                          |
| malware   | Busca signos de una infección malware en el host objetivo                                                                                    |
| safe      | Diseñado para no afectar al objetivo de manera negativa                                                                                      |
| version   | Mide la versión del software o protocolo usado por el host objetivo                                                                          |
| vul       | Busca si los sistemas objetivos, tienen alguna vulnerabilidad conocida                                                                       |
