# Practica Guiada 2 - Tiempo Real

Este repositorio contiene el código de la práctica guiada "Tiempo Real" de la
asignatura Software Avanzado Radar (SARA) del Master en Sistemas Radar.

El repositorio contiene las siguientes carpetas:

- `app`: contiene el archivo main.py para ejecutar la aplicación y ficheros
relacionados con el código de la aplicación.
- `app/src`: contiene cada uno de los paquetes de python que usaremos durante el
  desarrollo de la práctica dividido de forma básica por las diferentes
  funcionalidades.
  - `actors`: contiene las distintas clases con la lógica de funcionamiento
  principal de la práctica
  - `helpers`: contiene archivos con funcionalidades generales del proyecto que
  pueden ser utilizada por cualquier clase principal.
  - `models`: contine clases que actuan como modelos de datos del proyecto.
  - `monitors`: contiene las clases relacionadas con la implementación de los
  monitores de la práctica.

## Escenario de la práctica

El escenario de la práctica consiste en una implementación de un modelo
digital de un radar. Además del modelo del radar también existe un modelo
digital de puntos con distintas características que pueden ser detectados por
el radar. Para más detalles sobre el proyecto se puede consultar la
[Práctica Guiada 1](https://github.com/SARA-MSRA-UPM/PG1_concurrencia).

## Ejecución

El primer paso para poder ejecutar la práctica y comprobar su funcionamiento
será la creación de un entorno virtual propio del proyecto. Normalmente el IDE
al no encontrar un entorno virtual creado preguntará automáticamente si se desea
crearlo. En cualquier caso se pude crear utilizando los siguientes comandos:

- Linux

```shell
python3 -m venv .venv
source .venv/bin/activate
```

- Windows

```powershell
python3 -m venv venv
venv\Scripts\Activate.ps1
```

Una vez creado el entorno virtual es necesario instalar las dependencias propias
del proyecto. Las dependencias están definidas en el fichero `requirements.txt`.
Generalmente hay opciones para instalarlas de forma automática desde el IDE,
pero también se pueden instalar manualmente utilizando el siguiente comando:

```shell
pip install -r requirements.txt
```

Por último tras instalar las dependencias necesarias en nuestro entorno virtual
podemos arrancar el proceso principal de nuestro proyecto ejecutando el fichero
`app/main.py`.

```shell
python3 app/main.py
```

## Objetivos a realizar

1. **Graficar dinámicamente los movimientos de radares y puntos** Durante esta
práctica utilizaremos un escenario con varios radares y puntos similar al final
de la [Práctica Entregable 1](https://github.com/SARA-MSRA-UPM/PE1_concurrencia)
. Sin embargo, en este caso nuestro objetivo será mostrar dinámicamente las
actualizaciones de los distintos agentes, radares y puntos. Para graficar los
distintos elementos utilizaremos la librería `matplotlib`. Esta librería nos
permite dibujar principalmente funciones o gráficas de datos, pero en este caso
lo utilizaremos como "motor de visualización".
   - Implementaremos la clase `MapView` que nos ayudará a realizar tareas
   comunes de visualización.
   - Modificaremos la clase Radar implementando los métodos que ayudan a
   la visualización realizando operaciones geométricas.
   - Modificaremos el proceso principal del programa para incluir las instancias
   de los objetos necesarios para la visualización.
