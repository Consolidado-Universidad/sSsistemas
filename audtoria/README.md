## Auditoría de vulnerabilidades y contramedidas

Un rapido diseño de software, en conjunto con un insuficiente testing al que se le somete, produce un software con vulnerabilidades. Estas vulnerabilidades pueden ser explotadas por atacantes para obtener información sensible, modificar datos, o simplemente para causar daño. Por lo tanto, es necesario realizar auditorías de seguridad para identificar y corregir estas vulnerabilidades.

Las grandes compañías de software, como Microsoft, Google, y Apple, tienen equipos de seguridad que se dedican a realizar auditorías de seguridad en sus productos. Sin embargo, la mayoría de las empresas no tienen los recursos para mantener un equipo de seguridad dedicado. Por lo tanto, es necesario externalizar la auditoría de seguridad a empresas especializadas.

Cuando se detecta un problema, es necesario aplicar contramedidas para mitigar el riesgo. Las contramedidas pueden ser técnicas, como parches de seguridad, o administrativas, como políticas de seguridad. Es importante que las contramedidas sean efectivas y que no introduzcan nuevas vulnerabilidades.

Los datos de los usuarios de la aplicación seran vulnerables en el transcurso del tiempo desde que se encuentre el fallo hasta que se aplique la contramedida. Por lo tanto, es importante que las contramedidas se apliquen lo antes posible.

### Buscar vulnerabilidades

Cuando un *hacker* planea realizar un ataque, planea una estrategia antes de realizar el ataque. Existen diferentes formas de penetrar a en sitio con acceso restringido. Su objetivo principal puede ser la conquista de una maquina remota o subida de privilegios. Para realizar un ataque, siempre hay que investigar primero a la víctima. Por ejemplo, que IP tienen los servidores, que puertos están abiertos, que servicios están corriendo, que software están utilizando, etc.

## Recomendaciones para tener un sistema seguro y libre de vulnerabilidades

Estar al día con las alertas de seguridad que saca tanto en *Bugtraq* como en las listas *CVE-CAN* 

Sitios Web recomendables:
- [unaaldia.hispasec.com](https://unaaldia.hispasec.com)
- [cve.mitre.org](https://cve.mitre.org)
- [nist](https://nvd.nist.gov/vuln/search)

## Exploits

El exploit funciona sólo con la versión de software que se ha probado. Si el software se actualiza, el exploit puede dejar de funcionar. Por lo tanto, es importante mantener el software actualizado para protegerse de los exploits.

Los exploits son herramientas que se diseñan para aprovechar vulnerabilidades específicas en sistemas o programas informáticos. Su funcionamiento varía según el error que se explote, las acciones que permita el bug, los objetivos en la máquina atacada y el shellcode que se desee ejecutar. Los resultados de utilizar un exploit pueden incluir la ejecución de comandos específicos, la desactivación de servicios o firewalls, la interrupción de procesos como la vigilancia de un antivirus, la generación de ataques DoS, el acceso a consolas del sistema operativo o la apertura de puertas traseras. El shellcode, generalmente escrito en ensamblador y codificado en hexadecimal, se almacena y ejecuta en la memoria del sistema operativo del dispositivo objetivo, permitiendo realizar múltiples acciones.

### Tipos de exploits

- **Exploits Locales**: Son aquellos que se ejecutan en la máquina local, es decir, en la máquina que está siendo atacada. Su objetivo es obtener privilegios de administrador o root en la máquina atacada.
- **Exploits Remotos**: Son aquellos que se ejecutan en una máquina remota, es decir, en una máquina que no está siendo atacada. Su objetivo es obtener acceso a la máquina atacada.
- **Ataques a través de una páqgina Web**: contienen código malicioso que se ejecuta en el navegador del usuario (payload). Este código puede ser JavaScript, Flash, Java, etc. El objetivo de estos ataques es obtener acceso a la máquina del usuario.
- **Ataque a un servicio que corre en un puerto**: El ataque a un servicio que opera en un puerto específico es uno de los métodos más habituales de explotación. Los exploits de este tipo funcionan enviando paquetes que contienen shellcode y los datos necesarios para explotar una vulnerabilidad a través de un puerto en el que el servicio afectado está activo. Además de permitir la carga de un payload en el sistema atacado, estos exploits también pueden usarse para realizar ataques de denegación de servicio (DoS) mediante el envío masivo de paquetes de datos de gran tamaño.
- **Ataque SQL Injection**: Los ataques de inyección SQL son una técnica de explotación que permite a un atacante ejecutar comandos SQL maliciosos en un servidor de base de datos. Estos ataques se producen cuando las aplicaciones web no validan correctamente las entradas de los usuarios antes de enviarlas a la base de datos. Los ataques de inyección SQL pueden tener graves consecuencias, como la eliminación de datos, la modificación de registros, la obtención de información confidencial o la ejecución de comandos en el sistema operativo subyacente.

