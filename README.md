# Practica Guiada 2 - Tiempo Real

Este repositorio contiene el código de la práctica guiada "Tiempo Real" de la 
asignatura Software Avanzado Radar (SARA) del Master en Sistemas Radar.

El repositorio contiene las siguientes carpetas:
- `app`: contiene el archivo main.py para ejecutar la aplicación y la carpeta
  `src` donde se sitúan el resto de archivos.
- `app/src`: contiene cada uno de los paquetes de python que usaremos durante
  el desarrollo de la práctica dividido de forma básica por las diferentes
  funcionalidades.
  - `actors`: contiene las distintas clases con la lógica de funcionamiento
    principal de la práctica
  - `helpers`: contiene archivos con funcionalidades generales del proyecto
    que pueden ser utilizadas por cualquier clase principal.
  - `base`: contiene clases base utilizadas en como núcleo de distintas
    funcionalidades del proyecto.
  - `graphics`: contiene las clases utilizadas para la visualización de los
    distintos datos y objetos del escenario.

## Escenario de la práctica
El escenario de la práctica consiste en una implementación de un modelo
digital de un radar. Además del modelo del radar también existe un modelo
digital de puntos con distintas características que pueden ser detectados por
el radar. Presenta la misma estructura e implementación que en la
[Práctica Guiada 1](https://github.com/SARA-MSRA-UPM/PG1_concurrencia).

## Ejecución
El primer paso para poder ejecutar la práctica y comprobar su funcionamiento
será la creación de un entorno virtual propio del proyecto. En PyCharm es
posible crear un entorno virtual mediante la interfaz gráfica. En caso
necesario los comandos son los siguientes.
```
# Linux
# Crear
python3 -m venv venv
# Activar
source venv/bin/activate
# Desactivar
deactivate

# Windows
# Crear
python3 -m venv venv
# Activar
venv\Scripts\activate.bat
venv\Scripts\Activate.ps1
# Desactivar
deactivate
```

Una vez creado el entorno virtual es necesario instalar las dependencias
propias del proyecto. Las dependencias están definidas en el fichero
`requirements.txt`. En PyCharm se pueden instalar las dependencias mediante la
interfaz gráfica. En caso necesario los comandos son los siguientes.
```
pip install -r requirements.txt
```

Por último tras instalar las dependencias necesarias en nuestro entorno
virtual podemos arrancar el proceso principal de nuestro proyecto ejecutando
el fichero `app/main.py`.
```
python3 app/main.py
```

## Objetivos a realizar
1. **Graficar dinámicamente los movimientos de radares y puntos** Durante 
esta práctica utilizaremos un escenario con varios radares y puntos similar al 
final de la 
[Práctica Guiada 1](https://github.com/SARA-MSRA-UPM/PG1_concurrencia). Sin 
embargo, en este caso nuestro objetivo será mostrar dinámicamente las 
actualizaciones de los distintos agentes, radares y puntos. Para graficar los 
distintos elementos utilizaremos la librería `matplotlib`. Esta librería nos 
permite dibujar principalmente funciones o gráficas de datos, pero en este 
caso lo utilizaremos como "motor de visualización".
   - Implementaremos la clase `MapView` que nos ayudará a realizar tareas 
   comunes de visualización.
   - Modificaremos la clase Radar de tal implementando los métodos que ayudan 
   a la visualización realizando operaciones geométricas.
   - Modificaremos el proceso principal del programa para incluir las 
   instancias de los objetos necesarios para la visualización.
