import numpy as np
import PIL.Image as Image
from skimage.metrics import structural_similarity
from manejador_bits import llenar_bits


def arnold_cat_map_iterador(imagen, iteraciones):
    copia_imagen = imagen.copy()
    width, height = copia_imagen.size

    for _ in range(iteraciones):
        copia_temp = copia_imagen.copy()
        for x in range(width):
            for y in range(height):
                nx = (2 * x + y) % width
                ny = (x + y) % height

                copia_imagen.putpixel(
                    (nx, height-ny-1), copia_temp.getpixel((x, height-y-1)))

        del copia_temp

    return copia_imagen


def arnold_cat_map(imagen: Image):
    # contador de iteraciones
    counter = 0
    # cargamos la imagen
    imagen = imagen.convert('L')

    # creamos la matriz de la imagen
    matriz_imagen = np.array(imagen)
    # creamos una copia de la imagen
    copia_imagen = imagen.copy()
    # creamos una copia que servira para guardar la imagen con menor correlacion
    imagen_menor_correlacion = imagen.copy()
    # obtenemos las dimensiones de la imagen
    width, height = copia_imagen.size

    # variables para guardar la menor correlacion y el numero de iteracion en la que se encontro
    min = 1
    counter_min = 0

    # variable para controlar el ciclo (similar a un do-while)
    condicion = True

    while condicion:
        counter += 1

        # se aplica la transformacion de arnold cat map a la imagen copia
        copia_temp = copia_imagen.copy()
        for x in range(width):
            for y in range(height):
                nx = (2 * x + y) % width
                ny = (x + y) % height

                copia_imagen.putpixel(
                    (nx, height-ny-1), copia_temp.getpixel((x, height-y-1)))

        del copia_temp

        # creamos la matriz de la imagen copia
        matriz_copia_imagen = np.array(copia_imagen)

        # comparamos las matrices de la imagen original y la copia
        if np.array_equal(matriz_imagen, matriz_copia_imagen):
            condicion = False

        correlacion, _ = structural_similarity(
            matriz_imagen, matriz_copia_imagen, full=True)

        if correlacion < min:
            min = correlacion
            counter_min = counter
            imagen_menor_correlacion = copia_imagen.copy()

    return counter-counter_min, sustituir_bits(imagen_menor_correlacion)


def sustituir_bits(imagen: Image):
    # esta funcion sirve para quitar los dos bits de cada pixel y colocarlos con 00
    # se obtienen las dimensiones de la imagen
    width, height = imagen.size

    for x in range(width):
        for y in range(height):
            # obtenemos el pixel
            pixel = imagen.getpixel((x, y))
            pixel = bin(pixel)[2:]

            if len(pixel) < 8:
                pixel = llenar_bits(pixel, 8)

            if pixel[-2:] != '00':
                pixel = pixel[:-2] + '00'

                # sustituimos el pixel
                imagen.putpixel((x, y), int(pixel, 2))

    return imagen
