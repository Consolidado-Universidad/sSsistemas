# Guía de `iptables`

## Introducción

`iptables` es una herramienta de administración de paquetes para los sistemas operativos Linux que permite configurar las reglas del firewall. Es una interfaz de línea de comandos que interactúa con el framework de filtrado de paquetes del kernel de Linux.

## Conceptos Básicos

### Cadenas (Chains)

En `iptables`, una cadena es una lista de reglas que aplican a los paquetes que coinciden con ciertas condiciones. Las principales cadenas predeterminadas son:

- **INPUT:** Maneja los paquetes destinados a la máquina local.
- **OUTPUT:** Maneja los paquetes generados desde la máquina local y que salen de ella.
- **FORWARD:** Maneja los paquetes que pasan a través de la máquina (no destinados a ella ni originados por ella).
- **PREROUTING:** Modifica los paquetes tan pronto como llegan y antes de que se enruten. Utilizado en la tabla `nat`.
- **POSTROUTING:** Modifica los paquetes justo antes de que salgan de la interfaz de red. Utilizado en la tabla `nat`.

### Tablas (Tables)

Las tablas en `iptables` son colecciones de cadenas. Cada tabla está diseñada para un propósito específico:

- **filter:** La tabla por defecto que contiene las cadenas INPUT, OUTPUT, y FORWARD.
- **nat:** Se utiliza para la traducción de direcciones de red (NAT). Contiene las cadenas PREROUTING, POSTROUTING, y OUTPUT.
- **mangle:** Se utiliza para la modificación de paquetes.
- **raw:** Se utiliza para configuraciones que no deben ser sujetas al seguimiento de conexión.
- **security:** Se utiliza para aplicar políticas de seguridad (por ejemplo, SELinux).

### Políticas por Defecto

Las políticas por defecto definen el comportamiento de una cadena si un paquete no coincide con ninguna regla en esa cadena. Las opciones comunes son:
- **ACCEPT:** Permite el paquete.
- **DROP:** Descartar el paquete silenciosamente.
- **REJECT:** Descartar el paquete y enviar una respuesta de error al emisor.