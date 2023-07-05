import PIL.Image as pil

ELEMENTOS = 256


def mapeo_pixel(imagen: pil, sbox: tuple):

    lienzo_imagen = imagen.copy()
    width, height = lienzo_imagen.size

    for x in range(width):
        for y in range(height):
            pixel = lienzo_imagen.getpixel((x, y))
            lienzo_imagen.putpixel((x, y), sbox[pixel])

    return lienzo_imagen


# se hara el mapeo de sboxes
# pero este será para coordenadas
# teniendo una imagen de nxn pixeles, se hara la sustitucion a otra coordenada
# con la s box

def mapeo_coordenadas(imagen: pil, sbox):
    # la sbox tiene 256 elementos, del 0 al 255
    
    # creamos el lienzo donde iremos pegando la imagen resultante
    lienzo_imagen = imagen.copy()
    width, height = lienzo_imagen.size

    # recorremos la imagen original en secciones de 255 de izquierda a derecha
    # arriba a bajo
    # factor de multiplicacion
    factor_x = 0
    factor_y = 0

    # vemos cuantas secciones tiene en x
    secciones_x = width // ELEMENTOS
    secciones_y = height // ELEMENTOS

    # realizamos el recorrido arriba a bajo
    while factor_y < secciones_y:
        factor_x = 0
        while factor_x < secciones_x:
            # recorremos la seccion
            for x in range(ELEMENTOS):
                for y in range(ELEMENTOS):
                    # obtenemos los valores de la sbox
                    x_sbox = sbox[x]
                    y_sbox = sbox[y]

                    # agregamos el pixel en el lienzo nuevo
                    try:
                        lienzo_imagen.putpixel(
                            ((factor_x*ELEMENTOS)+x_sbox, (factor_y*ELEMENTOS)+y_sbox), imagen.getpixel((x, y)))
                    except:
                        print("Error en el pixel: ", x, y)
                        print("al colocar en ", str((factor_x*ELEMENTOS)+x_sbox), str((factor_y*ELEMENTOS)+y_sbox) )
                        print(lienzo_imagen.size)
                        quit()
            # aumentamos el factor
            factor_x += 1
        factor_y += 1

    return lienzo_imagen