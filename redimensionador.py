import PIL.Image as Image

ELEMENTOS = 256

def redimensionar(imagen: Image, imagen_oculta: Image):
    # debemos dejar la imagen en multiplos de 255 pixeles mayores al original
    width, heigth = imagen.size

    # si no es multiplo de 255, se le suma la diferencia
    if width % ELEMENTOS != 0:
        width = width + (ELEMENTOS - (width % ELEMENTOS))
    if heigth % ELEMENTOS != 0:
        heigth = heigth + (ELEMENTOS - (heigth % ELEMENTOS))

    # redimensionamos la imagen
    imagen = imagen.resize((width, heigth))
    imagen_oculta = imagen_oculta.resize((width, heigth))

    # retornamos la imagen
    return imagen, imagen_oculta
