import s_boxes as sb
import numpy as np
import PIL.Image as pil


def mapeo(imagen: pil, sbox: tuple):

    lienzo_imagen = imagen.copy()
    width, height = lienzo_imagen.size

    for x in range(width):
        for y in range(height):
            pixel = lienzo_imagen.getpixel((x, y))
            valor_x = pixel % len(sbox[0])
            valor_y = pixel // len(sbox)
            lienzo_imagen.putpixel((x, y), sbox[valor_y][valor_x])

    return lienzo_imagen
