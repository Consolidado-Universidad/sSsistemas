Para aumentar la seguridad de un servidor conectado a Internet y con servicios web, MySQL y FTP, es crucial restringir el acceso únicamente a las direcciones IP y puertos necesarios. A continuación, se presentan las reglas adicionales que deben aplicarse:

### Políticas por Defecto

#### Políticas por Defecto para INPUT, OUTPUT y FORWARD
Establecemos una política por defecto más restrictiva:
```bash
# Establecer políticas por defecto más restrictivas
iptables -P INPUT DROP
iptables -P OUTPUT ACCEPT
iptables -P FORWARD DROP
```

### FLUSH de Reglas
Limpiamos todas las reglas existentes:

```bash
iptables -F
```
* Se utiliza para eliminar todas las reglas actuales en iptables antes de aplicar nuevas reglas. Es una buena práctica para evitar conflictos o redundancias.

```bash
iptables -X
```
* Se utiliza para limpiar cualquier cadena personalizada que haya sido creada, asegurando que solo las cadenas predeterminadas (INPUT, OUTPUT, FORWARD) permanezcan.

```bash
iptables -Z
```
* Se utiliza para reiniciar los contadores de estadísticas, útil para monitorear nuevas reglas desde cero.

```bash
iptables -t nat -F
```
* Se utiliza para eliminar todas las reglas de NAT (Network Address Translation) antes de aplicar nuevas reglas. Esto asegura que no haya reglas NAT conflictivas o redundantes.

### Reglas Básicas
Permitimos acceso a la IP del administrador, al DBA para MySQL, al operador para FTP y abrimos el puerto web (80):
```bash
# Permitir acceso completo a la IP del administrador (ejemplo: 192.168.0.1)
iptables -A INPUT -s 192.168.0.1 -j ACCEPT

# Permitir acceso al puerto MySQL (3306) para el DBA (ejemplo: 192.168.0.2)
iptables -A INPUT -p tcp -s 192.168.0.2 --dport 3306 -j ACCEPT

# Permitir acceso al puerto FTP (21) para el operador (ejemplo: 192.168.0.3)
iptables -A INPUT -p tcp -s 192.168.0.3 --dport 20,21 -j ACCEPT
"""
Necesidad del Servicio FTP:
Si el operador necesita transferir archivos hacia o desde el servidor, se requiere permitir el acceso al puerto 21 donde el servidor FTP escucha las conexiones de control.
"""

# Permitir acceso al puerto web (80) para todos
iptables -A INPUT -p tcp --dport 80 -j ACCEPT

# Permitir acceso al puerto HTTPS (443) para todos
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
```

### Reglas Adicionales para Seguridad

1. **Permitir tráfico de loopback (localhost):**
```bash
iptables -A INPUT -i lo -j ACCEPT
```
* Esta regla permite todo el tráfico entrante desde la interfaz de loopback (localhost). La interfaz de loopback es una interfaz de red virtual utilizada por el sistema operativo para comunicarse consigo mismo. La dirección IP asociada comúnmente con esta interfaz es 127.0.0.1.

2. **Permitir conexiones establecidas y relacionadas:**
```bash
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
```
* Permitir conexiones establecidas y relacionadas es una regla fundamental en la configuración de un firewall porque ayuda a asegurar que el tráfico no solicitado no pueda acceder a tu red interna. Esta regla permite que las respuestas a las solicitudes salientes y las conexiones establecidas se procesen sin problemas.

3. **Permitir ICMP (ping) de forma limitada:**
```bash
iptables -A INPUT -p icmp -m limit --limit 1/s --limit-burst 5 -j ACCEPT
```
* Esta regla permite los paquetes ICMP, que son utilizados para mensajes de control de red como ping, pero los limita para prevenir abusos como ataques de denegación de servicio (DoS).

4. **Limitar el acceso SSH (puerto 22) solo desde direcciones IP específicas (ejemplo: 192.168.0.4):**
```bash
iptables -A INPUT -p tcp -s 192.168.0.4 --dport 22 -j ACCEPT
```
* Esta regla permite el acceso SSH (puerto 22) solo desde la dirección IP específica 192.168.0.4. Esto significa que solo el dispositivo con la IP 192.168.0.4 podrá iniciar una conexión SSH con el servidor.

5. **Registrar y rechazar todo el tráfico no permitido:**
```bash
iptables -A INPUT -j LOG --log-prefix "IPTables-Dropped: "
iptables -A INPUT -j REJECT
```
* Estas reglas primero registran los paquetes que no coinciden con ninguna regla permitida y luego los rechazan. Esto es útil para el diagnóstico y la seguridad, ya que proporciona un registro de los intentos de acceso no autorizados y asegura que estos paquetes sean rechazados de manera activa.

6. **Bloquear puertos no utilizados:**
```bash
# Bloquear todos los demás puertos no utilizados explícitamente
iptables -A INPUT -p tcp --dport 1:19 -j DROP
iptables -A INPUT -p tcp --dport 23:79 -j DROP
iptables -A INPUT -p tcp --dport 81:442 -j DROP
iptables -A INPUT -p tcp --dport 444:65535 -j DROP
```
* Estas reglas bloquean todos los paquetes entrantes a través del protocolo TCP que se dirigen a puertos no utilizados explícitamente dentro de los rangos especificados. Esto mejora la seguridad al reducir la superficie de ataque de la máquina, asegurando que solo los puertos necesarios estén abiertos y accesibles.


### Ejemplo Completo
```bash
echo -n "Aplicando Reglas de Firewall..."

# FLUSH de reglas
iptables -F
iptables -X
iptables -Z
iptables -t nat -F

# Políticas por defecto
iptables -P INPUT DROP
iptables -P OUTPUT ACCEPT
iptables -P FORWARD DROP

# Permitir tráfico loopback
iptables -A INPUT -i lo -j ACCEPT

# Permitir conexiones establecidas y relacionadas
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Permitir ICMP (ping) de forma limitada
iptables -A INPUT -p icmp -m limit --limit 1/s --limit-burst 5 -j ACCEPT

# Permitir acceso completo a la IP del administrador
iptables -A INPUT -s 192.168.0.1 -j ACCEPT

# Permitir acceso al puerto MySQL (3306) para el DBA
iptables -A INPUT -p tcp -s 192.168.0.2 --dport 3306 -j ACCEPT

# Permitir acceso al puerto FTP (21) para el operador
iptables -A INPUT -p tcp -s 192.168.0.3 --dport 21 -j ACCEPT

# Permitir acceso al puerto web (80) para todos
iptables -A INPUT -p tcp --dport 80 -j ACCEPT

# Permitir acceso al puerto HTTPS (443) para todos
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Limitar el acceso SSH (puerto 22) solo desde direcciones IP específicas
iptables -A INPUT -p tcp -s 192.168.0.4 --dport 22 -j ACCEPT

# Registrar y rechazar todo el tráfico no permitido
iptables -A INPUT -j LOG --log-prefix "IPTables-Dropped: "
iptables -A INPUT -j REJECT

# Bloquear puertos no utilizados
iptables -A INPUT -p tcp --dport 1:19 -j DROP
iptables -A INPUT -p tcp --dport 23:79 -j DROP
iptables -A INPUT -p tcp --dport 81:442 -j DROP
iptables -A INPUT -p tcp --dport 444:65535 -j DROP

echo "Reglas de Firewall aplicadas."
```

Estas reglas proporcionan una configuración de firewall básica pero segura, protegiendo los servicios web, MySQL y FTP, y restringiendo el acceso solo a las direcciones IP y puertos necesarios.