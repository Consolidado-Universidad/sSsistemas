Para mejorar la seguridad del esquema y proteger la red interna utilizando una DMZ (Zona Desmilitarizada), se deben establecer reglas específicas en el firewall. Aquí está la configuración recomendada basada en los requisitos que has mencionado.

### Configuración del Firewall para DMZ

#### 1. Establecer las políticas por defecto

```bash
# Establecer políticas por defecto más restrictivas
iptables -P INPUT DROP
iptables -P OUTPUT ACCEPT
iptables -P FORWARD DROP
iptables -t nat -P PREROUTING ACCEPT
iptables -t nat -P POSTROUTING ACCEPT
```

#### 2. FLUSH de reglas
```bash
# Limpiar reglas existentes
iptables -F
iptables -X
iptables -Z
iptables -t nat -F
```

#### 3. Permitir tráfico esencial

**Permitir tráfico de loopback (localhost):**
```bash
iptables -A INPUT -i lo -j ACCEPT
```

**Permitir conexiones establecidas y relacionadas:**
```bash
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT
```

#### 4. Acceso de la red local a Internet
```bash
# Permitir acceso de la red local a Internet
iptables -A FORWARD -i eth1 -o eth0 -s 192.168.10.0/24 -j ACCEPT

# Enmascarar el tráfico saliente desde la LAN
iptables -t nat -A POSTROUTING -s 192.168.10.0/24 -o eth0 -j MASQUERADE
```

#### 5. Acceso público a los puertos HTTP (80) y HTTPS (443) del servidor en la DMZ
```bash
# Permitir tráfico HTTP y HTTPS a la DMZ
iptables -A FORWARD -p tcp -d 192.168.3.1 --dport 80 -j ACCEPT
iptables -A FORWARD -p tcp -d 192.168.3.1 --dport 443 -j ACCEPT

# Redirigir tráfico HTTP y HTTPS a la DMZ
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination 192.168.3.1:80
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j DNAT --to-destination 192.168.3.1:443
```

#### 6. Acceso del servidor en la DMZ a la base de datos en la LAN
```bash
# Permitir acceso a la base de datos desde la DMZ
iptables -A FORWARD -p tcp -s 192.168.3.1 -d 192.168.10.2 --dport 3306 -j ACCEPT
```

#### 7. Bloquear el resto de acceso de la DMZ hacia la LAN
```bash
# Bloquear todo el tráfico de la DMZ hacia la LAN excepto lo permitido
iptables -A FORWARD -s 192.168.3.0/24 -d 192.168.10.0/24 -j DROP
```

### Problemas del Esquema Anterior (Sin DMZ)

Si el servidor web en la red local es hackeado, el atacante podría tener acceso a la red interna, comprometiendo otros servicios y dispositivos. Además, los ataques desde el servidor comprometido podrían propagarse a otros sistemas dentro de la LAN.

### Soluciones con DMZ

Usar una DMZ proporciona una capa adicional de seguridad al separar los servicios accesibles desde Internet (como el servidor web) de la red interna. Esto reduce el riesgo de que un atacante comprometa la red interna si el servidor en la DMZ es hackeado.

### Resumen de Reglas Necesarias

1. **Permitir acceso de la red local a Internet.**
2. **Permitir acceso público a los puertos HTTP (80) y HTTPS (443) del servidor en la DMZ.**
3. **Permitir acceso del servidor en la DMZ a la base de datos en la LAN.**
4. **Bloquear todo el tráfico de la DMZ hacia la LAN, excepto el tráfico permitido.**

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
iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT

# Permitir acceso de la red local a Internet
iptables -A FORWARD -i eth1 -o eth0 -s 192.168.10.0/24 -j ACCEPT

# Enmascarar el tráfico saliente desde la LAN
iptables -t nat -A POSTROUTING -s 192.168.10.0/24 -o eth0 -j MASQUERADE

# Permitir tráfico HTTP y HTTPS a la DMZ
iptables -A FORWARD -p tcp -d 192.168.3.1 --dport 80 -j ACCEPT
iptables -A FORWARD -p tcp -d 192.168.3.1 --dport 443 -j ACCEPT

# Redirigir tráfico HTTP y HTTPS a la DMZ
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination 192.168.3.1:80
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j DNAT --to-destination 192.168.3.1:443

# Permitir acceso a la base de datos desde la DMZ
iptables -A FORWARD -p tcp -s 192.168.3.1 -d 192.168.10.2 --dport 3306 -j ACCEPT

# Bloquear todo el tráfico de la DMZ hacia la LAN excepto lo permitido
iptables -A FORWARD -s 192.168.3.0/24 -d 192.168.10.0/24 -j DROP

echo "Reglas de Firewall aplicadas."
```

Con estas reglas, el firewall configurará una DMZ segura que permite el acceso controlado desde Internet al servidor web, permite que el servidor en la DMZ acceda a la base de datos en la LAN y bloquea cualquier otro acceso de la DMZ a la LAN, mejorando así la seguridad del esquema de red.