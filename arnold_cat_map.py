import numpy as np
from PIL.Image import open as load_pic

def arnold_cat_map(path):
    # contador de iteraciones
    counter = 0
    # cargamos la imagen
    imagen = load_pic(path)
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

                copia_imagen.putpixel((nx, height-ny-1), copia_temp.getpixel((x, height-y-1)))

        del copia_temp

        # creamos la matriz de la imagen copia
        matriz_copia_imagen = np.array(copia_imagen)
        
        # comparamos las matrices de la imagen original y la copia
        if np.array_equal(matriz_imagen, matriz_copia_imagen):
            condicion = False
        
        # sacamos la correlacion entre las dos dimensiones de la matriz
        correlacion = np.corrcoef(matriz_imagen.flatten(), matriz_copia_imagen.flatten())[0, 1]
        if correlacion < min:
            min = correlacion
            counter_min = counter
            imagen_menor_correlacion = copia_imagen.copy()


    return counter, counter_min, imagen_menor_correlacion
