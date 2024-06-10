## Configuración de Firewall para la Red LAN

El esquema de red presentado utiliza un firewall para proteger la red LAN y controlar el acceso a Internet. A continuación, se describen las configuraciones necesarias y los problemas potenciales de este esquema.

### Configuración Necesaria

#### 1. Acceso desde la Red Local

```bash
# Permitir acceso desde la red local
iptables -A INPUT -s 192.168.10.0/24 -i eth1 -j ACCEPT
```

#### 2. Redirecciones
   
```bash
# Redirigir tráfico del puerto 80 al servidor interno
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination 192.168.10.12:80

# Redirigir tráfico del puerto 3389 desde una IP específica al servidor interno
iptables -t nat -A PREROUTING -s 221.23.124.181 -i eth0 -p tcp --dport 3389 -j DNAT --to-destination 192.168.10.12:3389

```
#### 3. Abrir Puertos de Correo

```bash
# Abrir puerto 25 (SMTP)
iptables -A INPUT -s 0.0.0.0/0 -p tcp --dport 25 -j ACCEPT

# Abrir puerto 110 (POP3)
iptables -A INPUT -s 0.0.0.0/0 -p tcp --dport 110 -j ACCEPT

# Abrir puerto 1723 (PPTP) para una IP específica
iptables -A INPUT -s 211.45.176.24 -p tcp --dport 1723 -j ACCEPT
```

#### 4. Permitir Acceso a Servicios Web y DNS desde la LAN
```bash
# Permitir tráfico HTTP desde la LAN
iptables -A FORWARD -s 192.168.10.0/24 -i eth1 -p tcp --dport 80 -j ACCEPT

# Permitir tráfico HTTPS desde la LAN
iptables -A FORWARD -s 192.168.10.0/24 -i eth1 -p tcp --dport 443 -j ACCEPT

# Permitir consultas DNS desde la LAN
iptables -A FORWARD -s 192.168.10.0/24 -i eth1 -p tcp --dport 53 -j ACCEPT
iptables -A FORWARD -s 192.168.10.0/24 -i eth1 -p udp --dport 53 -j ACCEPT

# Denegar todo el tráfico restante desde la LAN
iptables -A FORWARD -s 192.168.10.0/24 -i eth1 -j DROP

```

#### 5. Configurar NAT y Habilitar el Bit de Forwarding
El enmascaramiento (masquerading) permite que múltiples dispositivos en una red local (LAN) compartan una única dirección IP pública, facilitando el acceso a Internet. Por ejemplo, si tienes una red interna `192.168.10.0/24` y una conexión a Internet a través de la interfaz `eth0`, la regla de enmascaramiento permite que todos los dispositivos en `192.168.10.0/24` accedan a Internet utilizando la dirección IP pública de `eth0`.

```bash
# Configuración de NAT en la cadena POSTROUTING para enmascarar tráfico saliente
iptables -t nat -A POSTROUTING -s 192.168.10.0/24 -o eth0 -j MASQUERADE
```
Bit de Forwarding: Una configuración en las interfaces de red que determina si el sistema debe reenviar paquetes entre diferentes interfaces de red.
Propósito: Permitir que un sistema Linux actúe como un router, encaminando tráfico de una red a otra.

#### 6. Cerramos el rango de puerto bien conocido

```bash
# Cerrar el rango de puertos bien conocidos (0-1024) para TCP
iptables -A INPUT -s 0.0.0.0/0 -p tcp --dport 1:1024 -j DROP

# Cerrar el rango de puertos bien conocidos (0-1024) para UDP
iptables -A INPUT -s 0.0.0.0/0 -p udp --dport 1:1024 -j DROP

# Cerrar el puerto 1723 para PPTP excepto para la IP específica del jefe
iptables -A INPUT -s 0.0.0.0/0 -i eth0 -p tcp --dport 1723 -j DROP
```

### Problemas Potenciales del Esquema

1. **Seguridad Insuficiente:**
   - **Telnet:** Telnet no es seguro ya que transmite los datos en texto claro, lo que lo hace vulnerable a la intercepción. Es recomendable usar SSH en lugar de Telnet.
   - **Puertos Abiertos:** Tener múltiples servicios abiertos (SMTP, POP3, PPTP) puede aumentar la superficie de ataque. Cada servicio expuesto es un posible punto de entrada para atacantes.

2. **Rendimiento del Firewall:**
   - **Carga de Procesamiento:** El firewall tendrá que manejar el NAT y el filtrado de paquetes, lo que puede ser una carga considerable dependiendo del volumen de tráfico.

3. **Complejidad de la Configuración:**
   - **Doble NAT:** La configuración de doble NAT puede complicar el diagnóstico de problemas de conectividad y puede introducir latencia adicional.

4. **Gestión Centralizada:**
   - **Punto Único de Falla:** El firewall se convierte en un punto único de falla. Si el firewall falla, toda la conectividad de la red LAN a Internet se verá interrumpida.

5. **Acceso Interno:**
   - **Políticas de Seguridad Interna:** No hay indicación de políticas de seguridad interna para proteger la LAN contra amenazas internas. Es crucial implementar reglas que limiten el tráfico dentro de la LAN misma.

6. **Logs y Monitoreo:**
   - **Falta de Monitoreo:** No hay mención de registro y monitoreo del tráfico, lo cual es crucial para detectar y responder a posibles incidentes de seguridad.

### Soluciones y Recomendaciones

1. **Seguridad Mejorada:**
   - **Usar SSH en lugar de Telnet:** Configurar el acceso remoto usando SSH para una mayor seguridad.
   - **Revisar Puertos Abiertos:** Solo abrir los puertos necesarios y utilizar herramientas de auditoría de seguridad para revisar regularmente las configuraciones.

2. **Optimización del Firewall:**
   - **Hardware Adecuado:** Asegurarse de que el hardware del firewall pueda manejar el volumen de tráfico esperado sin degradar el rendimiento.

3. **Simplificación de NAT:**
   - **Simplificar la Configuración:** Evaluar si el doble NAT es realmente necesario o si se puede simplificar la topología de red.

4. **Monitoreo y Respuesta:**
   - **Implementar Logging:** Habilitar el registro de tráfico y utilizar herramientas de monitoreo para identificar y responder a incidentes de seguridad.

5. **Seguridad Interna:**
   - **Políticas de Segmentación:** Implementar políticas de segmentación de la red para limitar el tráfico entre dispositivos en la LAN.

Con estas medidas, se puede mejorar significativamente la seguridad y la eficiencia del esquema de red presentado.

-----------------------------------------------
**NAT entre el router y el firewall:**
```bash
# Enmascarar el tráfico saliente desde la red interna hacia el router
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

**NAT entre el firewall y la red LAN:**
```bash
# Enmascarar el tráfico saliente desde la LAN hacia el firewall
iptables -t nat -A POSTROUTING -s 192.168.1.0/24 -o eth1 -j MASQUERADE
```
