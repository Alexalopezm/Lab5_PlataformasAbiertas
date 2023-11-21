# Lab5_PlataformasAbiertas
## Universidad de Costa Rica
### IE 0117 - Programación Bajo Plataformas Abiertas
#### Laboratorio 5: Manipulación de Imágenes con Python (segundo ciclo del 2023)
##### Integrantes:
- Alexa López Marcos, B94353
- Manfred Soza Garcia, B97755
- Frank Wang Wu, B57946

- # Código `LAB5.py`
Descripción: El presente laboratorio se quiere realizar una manipulación de imágenes que permite abrir una imagen y hacerlo en una display. Por lo que se va a utilizar una serie de bibliotecas para abrir dicha imagen.

## Paquetes importados 
### argparse
Un módulo que facilita la creación de interfaces de línea de comandos. En este archivo se utiliza para analizar los argumentos pasados por la línea de comandos.

### PIL (Python Imaging Library)
Es una biblioteca que se utiliza para manipular imágenes, para abrir y mostrar imágenes en formato de mapa de bits.

### matplotlib.pyplot
Es una biblioteca de visualización de datos en Python, que se utilizaría en este contexto para abrir y mostrar imágenes.

### cv2 (OpenCV)
Es una biblioteca de visión por computadora que proporciona una amplia gama de herramientas para procesar imágenes y videos, por lo que este cargar y mostrar imágenes en ventanas.

## Funciones 
### clase 'ImageProcessor'
#### 1. '__init__(self, library)'
El constructor de la clase ImageProcessor que inicializa un objeto ImageProcessor con la biblioteca especificada ('PIL', 'Matplotlib', 'OpenCV').

#### 2. 'mostrar_imagen(self, ruta)'
Método para mostrar la imagen utilizando la biblioteca especificada.

### Funciones de visualización de imágenes para cada biblioteca
