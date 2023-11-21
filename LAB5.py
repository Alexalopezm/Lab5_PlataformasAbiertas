import argparse         # Se utiliza para manejar los argumentos de la línea de comandos
# Se importan las librerias necesarias para el laboratorio
from PIL import Image
import matplotlib.pyplot as plt
import cv2


class ImageProcessor:
    def _init_(self, library):
        # Inicialización de la clase ImageProcessor con la biblioteca especificada.
        self.library = library

    def mostrar_imagen(self, ruta):
        # Método para mostrar una imagen utilizando la biblioteca seleccionada.
        if self.library == 'PIL':
            # Si se selecciona PIL, se llama al método mostrar_imagen_pil().
            self.mostrar_imagen_pil(ruta)
        elif self.library == 'Matplotlib':
            # Si se selecciona Matplotlib, se llama al método mostrar_imagen_matplotlib().
            self.mostrar_imagen_matplotlib(ruta)
        elif self.library == 'OpenCV':
            # Si se selecciona OpenCV, se llama al método mostrar_imagen_opencv().
            self.mostrar_imagen_opencv(ruta)
        else:
            # Si la biblioteca no es válida, se muestra un mensaje de error.
            print("Biblioteca no válida. Selecciona PIL, Matplotlib u OpenCV.")

    def mostrar_imagen_pil(self, ruta):
        # Método para mostrar una imagen utilizando la biblioteca PIL.
        imagen = Image.open(ruta)
        imagen.show()

    def mostrar_imagen_matplotlib(self, ruta):
        # Método para mostrar una imagen utilizando la biblioteca Matplotlib.
        imagen = plt.imread(ruta)
        plt.imshow(imagen)
        plt.show()

    def mostrar_imagen_opencv(self, ruta):
        # Método para mostrar una imagen utilizando la biblioteca OpenCV.
        imagen = cv2.imread(ruta)
        cv2.imshow('Imagen', imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def parse_args():
    # Crea un objeto ArgumentParser para manejar los argumentos de línea de comandos.
    parser = argparse.ArgumentParser(description="Procesamiento de Imagenes")
    # Agrega un argumento "--biblioteca" para especificar la biblioteca a utilizar.
    parser.add_argument("--biblioteca", choices=["PIL", "Matplotlib", "OpenCV"], required=True,
                        help="Selecciona la biblioteca de procesamiento de imágenes")
    # Agrega un argumento "--imagen" para especificar la ruta de la imagen a procesar.
    parser.add_argument("--imagen", required=True, help="Ruta de la imagen a procesar")
    # Analiza los argumentos pasados desde la línea de comandos y los retorna.
    return parser.parse_args()


def main():
    # Obtiene los argumentos de línea de comandos utilizando la función parse_args().
    args = parse_args()
    try:
        # Crea una instancia de ImageProcessor con la biblioteca especificada en los argumentos.
        procesador = ImageProcessor(args.biblioteca)
        # Llama al método mostrar_imagen() del ImageProcessor con la ruta de la imagen.
        procesador.mostrar_imagen(args.imagen)
    except FileNotFoundError:
        # Maneja una excepción si el archivo de imagen no se encuentra en la ruta especificada.
        print(f"Error: Archivo no encontrado en la ruta especificada: {args.imagen}")
    except Exception as e:
        # Maneja cualquier otra excepción que pueda ocurrir durante el procesamiento de la imagen.
        print(f"Error al procesar la imagen: {e}")


if _name_ == "_main_":
    # Ejecuta la función main() si este script es el programa principal que se está ejecutando.
    main()
