# Sistema L con Turtle en Python

Este es un programa en Python que utiliza la biblioteca Turtle para graficar un sistema L o sistema de Lindenmayer, permitiendo al usuario ingresar el axioma, las reglas y otros parámetros.

## Requisitos

- Python 3.x
- Turtle (incluido en la biblioteca estándar de Python)

## Instrucciones de Uso

1. Clona el repositorio o descarga el archivo ZIP.
2. Ejecuta el script `L-system.py`.

## Personalización

Puedes personalizar el comportamiento del sistema L ajustando las siguientes variables en el script:

- `axioma`: Define el axioma inicial del sistema L.
- `reglas`: Especifica las reglas de producción para cada símbolo.
- `iteraciones`: Número de iteraciones para aplicar las reglas y generar la cadena final.
- `angulo`: Ángulo de giro en grados.
- `distancia`: Distancia para avanzar al dibujar el sistema L.

## Ejemplo

Aquí hay un ejemplo de configuración:

axioma = 'F'
reglas = {'F': 'C0FF-[C1-F+F+F]+[C2+F-F-F]'}
iteraciones = 5
angulo = 22
distancia = 10

Este genera un L-system parecido a una rama de arbol.
