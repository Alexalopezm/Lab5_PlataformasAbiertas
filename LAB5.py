import argparse
from PIL import Image
import matplotlib.pyplot as plt
import cv2

class ImageProcessor:
    def __init__(self, library):
        self.library = library

    def mostrar_imagen(self, ruta):
        if self.library == 'PIL':
            self.mostrar_imagen_pil(ruta)
        elif self.library == 'Matplotlib':
            self.mostrar_imagen_matplotlib(ruta)
        elif self.library == 'OpenCV':
            self.mostrar_imagen_opencv(ruta)
        else:
            print("Biblioteca no válida. Selecciona PIL, Matplotlib u OpenCV.")

    def mostrar_imagen_pil(self, ruta):
        imagen = Image.open(ruta)
        imagen.show()

    def mostrar_imagen_matplotlib(self, ruta):
        imagen = plt.imread(ruta)
        plt.imshow(imagen)
        plt.show()

    def mostrar_imagen_opencv(self, ruta):
        imagen = cv2.imread(ruta)
        cv2.imshow('Imagen', imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def parse_args():
    parser = argparse.ArgumentParser(description="Procesamiento de Imagenes")
    parser.add_argument("--biblioteca", choices=["PIL", "Matplotlib", "OpenCV"], required=True,
                        help="Selecciona la biblioteca de procesamiento de imágenes")
    parser.add_argument("--imagen", required=True, help="Ruta de la imagen a procesar")
    return parser.parse_args()

def main():
    args = parse_args()
    try:
        procesador = ImageProcessor(args.biblioteca)
        procesador.mostrar_imagen(args.imagen)
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en la ruta especificada: {args.imagen}")
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")

if __name__ == "__main__":
    main()