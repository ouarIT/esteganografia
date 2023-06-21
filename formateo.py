import PIL.Image as Image


def incrustacion(imagen: Image, diferencia: int):
    # pasamos a bits la diferencia
    diferencia_bin = bin(diferencia)[2:]

    # agregamos 0 a la izquierda hasta que sea multiplo de 8 asi se crea el pixel
    while len(diferencia_bin) < 12:
        diferencia_bin = '0' + diferencia_bin

    pixel1_bin = diferencia_bin[:6]
    pixel2_bin = diferencia_bin[6:]

    # agregamos los 0 menos significativos
    pixel1_bin = pixel1_bin + '00'
    pixel2_bin = pixel2_bin + '00'

    # cargamos los pixeles de la imagen
    imagen.putpixel((0, 0), int(pixel1_bin, 2))
    imagen.putpixel((0, 1), int(pixel2_bin, 2))

    # regresamos la imagen
    return imagen
