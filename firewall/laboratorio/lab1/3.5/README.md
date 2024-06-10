### Configuración de Firewall con DMZ para Mejorar la Seguridad de la Red

#### Contexto
La configuración de un firewall para proteger la red LAN y controlar el acceso a Internet se torna insegura si no se implementan medidas adicionales como una DMZ (Zona Desmilitarizada). La DMZ permite aislar los servicios públicos del resto de la red, reduciendo el riesgo de comprometer la red interna en caso de que un servidor público sea hackeado.

#### Objetivos de la Configuración
1. Acceso de la red local a Internet.
2. Acceso público al puerto TCP/80 y TCP/443 del servidor de la DMZ.
3. Acceso del servidor de la DMZ a una base de datos en la LAN.
4. Bloquear el resto del acceso de la DMZ hacia la LAN.

### Reglas Necesarias para Filtrar el Tráfico entre la DMZ y la LAN

#### FLUSH de Reglas Anteriores
```bash
iptables -F
iptables -X
iptables -Z
iptables -t nat -F
```

#### Establecer Políticas por Defecto
```bash
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -t nat -P PREROUTING ACCEPT
iptables -t nat -P POSTROUTING ACCEPT
```

#### Redirecciones y NAT
```bash
# Redirigir tráfico del puerto 80 a la máquina interna
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to 192.168.3.2:80

# Redirigir tráfico del puerto 443 a la máquina interna
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j DNAT --to 192.168.3.2:443

# Permitir conexiones locales al firewall
iptables -A INPUT -i lo -j ACCEPT

# Permitir acceso al firewall desde la red local
iptables -A INPUT -s 192.168.10.0/24 -i eth1 -j ACCEPT

# Realizar el enmascaramiento de la red local y la DMZ
iptables -t nat -A POSTROUTING -s 192.168.10.0/24 -o eth0 -j MASQUERADE
iptables -t nat -A POSTROUTING -s 192.168.3.0/24 -o eth0 -j MASQUERADE

# Habilitar el bit de forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward
```

#### Permitir el Paso de la DMZ a la Base de Datos en la LAN
```bash
iptables -A FORWARD -s 192.168.3.2 -d 192.168.10.5 -p tcp --dport 5432 -j ACCEPT
iptables -A FORWARD -s 192.168.10.5 -d 192.168.3.2 -p tcp --sport 5432 -j ACCEPT
```

#### Permitir Acceso al Terminal Server de la DMZ desde la LAN
```bash
iptables -A FORWARD -s 192.168.10.0/24 -d 192.168.3.2 -p tcp --sport 1024:65535 --dport 3389 -j ACCEPT
iptables -A FORWARD -s 192.168.3.2 -d 192.168.10.0/24 -p tcp --sport 3389 --dport 1024:65535 -j ACCEPT
```

#### Bloquear Acceso de la DMZ a la LAN
```bash
iptables -A FORWARD -s 192.168.3.0/24 -d 192.168.10.0/24 -j DROP
```

#### Bloquear Acceso de la DMZ al Propio Firewall
```bash
iptables -A INPUT -s 192.168.3.0/24 -i eth2 -j DROP
```

#### Bloquear Accesos Indeseados desde el Exterior
```bash
# Cerrar el rango de puertos bien conocidos
iptables -A INPUT -s 0.0.0.0/0 -p tcp --dport 1:1024 -j DROP
iptables -A INPUT -s 0.0.0.0/0 -p udp --dport 1:1024 -j DROP

# Cerrar el puerto de gestión (Webmin)
iptables -A INPUT -s 0.0.0.0/0 -p tcp --dport 10000 -j DROP
```

### Problema con IPs Públicas en la DMZ

Si las máquinas de la DMZ tienen una IP pública, se debe tener cuidado de no permitir el FORWARD por defecto. En este caso, no es necesario realizar redirecciones de puerto, sino que basta con enrutar los paquetes para que lleguen a la DMZ. 

### Configuración Sugerida sin Redirecciones para IPs Públicas en la DMZ
```bash
# Permitir el tráfico de la red local a Internet
iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT
iptables -A FORWARD -i eth0 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT

# Permitir acceso público al puerto TCP/80 y TCP/443 del servidor de la DMZ
iptables -A FORWARD -i eth0 -p tcp --dport 80 -d 192.168.3.2 -j ACCEPT
iptables -A FORWARD -i eth0 -p tcp --dport 443 -d 192.168.3.2 -j ACCEPT

# Permitir acceso del servidor de la DMZ a la base de datos en la LAN
iptables -A FORWARD -s 192.168.3.2 -d 192.168.10.5 -p tcp --dport 5432 -j ACCEPT
iptables -A FORWARD -d 192.168.3.2 -s 192.168.10.5 -p tcp --sport 5432 -j ACCEPT

# Bloquear el resto del acceso de la DMZ hacia la LAN
iptables -A FORWARD -s 192.168.3.0/24 -d 192.168.10.0/24 -j DROP
```

### Resumen

Este conjunto de reglas establece un firewall seguro que utiliza una DMZ para proteger la red interna. Permite el acceso necesario a servicios públicos, mientras restringe el acceso no autorizado y asegura que el tráfico se maneje de manera segura.