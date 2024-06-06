A continuación, se presentan las reglas de `iptables` para cada uno de los puntos mencionados:

### 1. Añadir una regla a la cadena INPUT para aceptar todos los paquetes que se originan desde la dirección 192.168.106.200.
```bash
iptables -A INPUT -s 192.168.106.200 -j ACCEPT
```

### 2. Eliminar todos los paquetes que entren.
```bash
iptables -P INPUT DROP
```

### 3. Permitir la salida de paquetes.
```bash
iptables -P OUTPUT ACCEPT
```

### 4. Añadir una regla a la cadena INPUT para rechazar todos los paquetes que se originan desde la dirección 192.168.106.200.
```bash
iptables -A INPUT -s 192.168.106.200 -j REJECT
```

### 5. Añadir una regla a la cadena INPUT para rechazar todos los paquetes que se originan desde la dirección de red 192.168.0.0.
```bash
iptables -A INPUT -s 192.168.0.0/16 -j REJECT
```

### 6. Permitir el acceso al servidor web (puerto TCP 80).
```bash
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

### 7. Permitir el acceso a nuestro servidor FTP (puerto TCP 20 y 21).
```bash
iptables -A INPUT -p tcp --dport 20 -j ACCEPT
iptables -A INPUT -p tcp --dport 21 -j ACCEPT
```

### 8. Permitimos a la máquina con IP 192.168.106.200 conectarse por medio de SSH.
```bash
iptables -A INPUT -p tcp -s 192.168.106.200 --dport 22 -j ACCEPT
```

### 9. Rechazamos a la máquina con IP 192.168.106.200 conectarse por medio de Telnet.
```bash
iptables -A INPUT -p tcp -s 192.168.106.200 --dport 23 -j REJECT
```

### 10. Rechazamos todo el tráfico que ingrese a nuestra red LAN 192.168.0.0/24 desde una red remota, como Internet, a través de la interfaz eth0.
```bash
iptables -A INPUT -i eth0 -s 0.0.0.0/0 -d 192.168.0.0/24 -j REJECT
```

### 11. Cerramos el rango de puertos bien conocidos (1-1023) desde cualquier origen.
```bash
iptables -A INPUT -p tcp --dport 1:1023 -j REJECT
iptables -A INPUT -p udp --dport 1:1023 -j REJECT
```

### 12. Aceptamos que vayan de nuestra red 192.168.0.0/24 a un servidor web (puerto 80).
```bash
iptables -A FORWARD -s 192.168.0.0/24 -p tcp --dport 80 -j ACCEPT
```

### 13. Aceptamos que nuestra LAN 192.168.0.0/24 vaya a puertos HTTPS.
```bash
iptables -A FORWARD -s 192.168.0.0/24 -p tcp --dport 443 -j ACCEPT
```

### 14. Aceptamos que los equipos de nuestra red LAN 192.168.0.0/24 consulten los DNS, y denegamos todo el resto a nuestra red.
```bash
iptables -A FORWARD -s 192.168.0.0/24 -p tcp --dport 53 -j ACCEPT
iptables -A FORWARD -s 192.168.0.0/24 -p udp --dport 53 -j ACCEPT
iptables -A FORWARD -d 192.168.0.0/24 -j REJECT
```

### 15. Permitimos enviar y recibir e-mail a todos.
```bash
iptables -A INPUT -p tcp --dport 25 -j ACCEPT
iptables -A INPUT -p tcp --dport 587 -j ACCEPT
iptables -A INPUT -p tcp --dport 993 -j ACCEPT
iptables -A INPUT -p tcp --dport 995 -j ACCEPT
```

### 16. Cerramos el acceso de una red definida 192.168.3.0/24 a nuestra red LAN 192.168.2.0/24.
```bash
iptables -A FORWARD -s 192.168.3.0/24 -d 192.168.2.0/24 -j REJECT
```

### 17. Permitimos el tráfico TCP y UDP de un equipo específico 192.168.3.5 a un servicio (puerto 5432) que ofrece un equipo específico (192.168.0.5) y su respuesta.
```bash
iptables -A FORWARD -p tcp -s 192.168.3.5 -d 192.168.0.5 --dport 5432 -j ACCEPT
iptables -A FORWARD -p udp -s 192.168.3.5 -d 192.168.0.5 --dport 5432 -j ACCEPT
iptables -A FORWARD -p tcp -s 192.168.0.5 -d 192.168.3.5 --sport 5432 -j ACCEPT
iptables -A FORWARD -p udp -s 192.168.0.5 -d 192.168.3.5 --sport 5432 -j ACCEPT
```

### 18. Permitimos el paso de paquetes cuya conexión se encuentra establecida.
```bash
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT
```

Con estas reglas, hemos cubierto los escenarios mencionados para configurar el firewall con `iptables`.