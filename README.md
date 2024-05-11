
# Repositorio de Ciberseguridad

Este repositorio contiene herramientas y scripts de ciberseguridad diseñados para realizar análisis y pruebas de seguridad de redes.

## Pre-requisitos

Antes de comenzar, asegúrate de tener Python instalado en tu sistema. Este proyecto utiliza Python 3.6 o superior.

## Configuración del entorno virtual

Es recomendable utilizar un entorno virtual para ejecutar los scripts incluidos en este repositorio para evitar conflictos de dependencias. Sigue estos pasos para configurar y activar un entorno virtual:

### Instalación de virtualenv

Si aún no tienes instalado `virtualenv`, puedes instalarlo mediante pip:

```bash
pip install virtualenv
```

### Creación del entorno virtual

Para crear un entorno virtual, ejecuta:

```bash
virtualenv venv
```

Esto creará un nuevo directorio `venv` en tu proyecto donde se almacenarán todas las dependencias.

### Activación del entorno virtual

Para activar el entorno virtual en Windows, ejecuta:

```bash
venv\Scripts\activate
```

En sistemas basados en Unix o MacOS, utiliza:

```bash
source venv/bin/activate
```

Al activar el entorno virtual, tu terminal debería reflejar el cambio añadiendo `(venv)` al principio de la línea de comandos.

## Instalación de dependencias

Con el entorno virtual activado, instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

Este comando instalará todas las bibliotecas y paquetes necesarios listados en el archivo `requirements.txt`.

## Instalación de nmap

Este proyecto utiliza `nmap`, una herramienta esencial para la exploración de redes y auditoría de seguridad. Para instalar `nmap`, sigue las instrucciones específicas de tu sistema operativo.

### En Debian/Ubuntu

```bash
sudo apt-get install nmap
```

### En Red Hat/CentOS

```bash
sudo yum install nmap
```

### En macOS (con Homebrew)

```bash
brew install nmap
```

## Uso

Una vez instaladas todas las dependencias y configurado el entorno, estás listo para ejecutar los scripts del repositorio. Asegúrate de leer la documentación específica de cada script para entender su funcionamiento y opciones disponibles.

## Contribuciones

Las contribuciones a este repositorio son bienvenidas. Si deseas contribuir, por favor, envía un Pull Request con tus cambios para revisión.
