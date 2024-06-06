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
# Limpiar reglas existentes
iptables -F
iptables -X
iptables -Z
iptables -t nat -F
```

### Reglas Básicas
Permitimos acceso a la IP del administrador, al DBA para MySQL, al operador para FTP y abrimos el puerto web (80):
```bash
# Permitir acceso completo a la IP del administrador (ejemplo: 192.168.0.1)
iptables -A INPUT -s 192.168.0.1 -j ACCEPT

# Permitir acceso al puerto MySQL (3306) para el DBA (ejemplo: 192.168.0.2)
iptables -A INPUT -p tcp -s 192.168.0.2 --dport 3306 -j ACCEPT

# Permitir acceso al puerto FTP (21) para el operador (ejemplo: 192.168.0.3)
iptables -A INPUT -p tcp -s 192.168.0.3 --dport 21 -j ACCEPT

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

2. **Permitir conexiones establecidas y relacionadas:**
```bash
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
```

3. **Permitir ICMP (ping) de forma limitada:**
```bash
iptables -A INPUT -p icmp -m limit --limit 1/s --limit-burst 5 -j ACCEPT
```

4. **Limitar el acceso SSH (puerto 22) solo desde direcciones IP específicas (ejemplo: 192.168.0.4):**
```bash
iptables -A INPUT -p tcp -s 192.168.0.4 --dport 22 -j ACCEPT
```

5. **Registrar y rechazar todo el tráfico no permitido:**
```bash
iptables -A INPUT -j LOG --log-prefix "IPTables-Dropped: "
iptables -A INPUT -j REJECT
```

6. **Bloquear puertos no utilizados:**
```bash
# Bloquear todos los demás puertos no utilizados explícitamente
iptables -A INPUT -p tcp --dport 1:19 -j DROP
iptables -A INPUT -p tcp --dport 23:79 -j DROP
iptables -A INPUT -p tcp --dport 81:442 -j DROP
iptables -A INPUT -p tcp --dport 444:65535 -j DROP
```

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