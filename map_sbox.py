import PIL.Image as pil


def mapeo(imagen: pil, sbox: tuple):

    lienzo_imagen = imagen.copy()
    width, height = lienzo_imagen.size

    for x in range(width):
        for y in range(height):
            pixel = lienzo_imagen.getpixel((x, y))
            lienzo_imagen.putpixel((x, y), sbox[pixel])

    return lienzo_imagen
