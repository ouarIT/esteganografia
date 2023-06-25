import PIL.Image as pil


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

def mapeo_coordenadas(imagen: pil, sbox: tuple(tuple)):
    
        lienzo_imagen = imagen.copy()
        width, height = lienzo_imagen.size
    
        for x in range(width):
            for y in range(height):
                # para la coordenada en x obtenmos sus valores sbox
                x_x = x % len(sbox)
                x_y = x // len(sbox)

                # para la coordenada en y
                y_x = y % len(sbox)
                y_y = y // len(sbox)

                # obtenemos los valores de la sbox
                x_sbox = sbox[x_x][x_y]
                y_sbox = sbox[y_x][y_y]

                # agregamos el pixel en el lienzo nuevo
                lienzo_imagen.putpixel((x_sbox, y_sbox), imagen.getpixel((x, y)))

        return lienzo_imagen

def mapeo_coordenadas_lineal(imagen: pil, sbox: tuple(tuple)):
    
        lienzo_imagen = imagen.copy()
        width, height = lienzo_imagen.size
    
        for x in range(width):
            for y in range(height):
                # obtenemos los valores de la sbox
                x_sbox = sbox[x]
                y_sbox = sbox[y]

                # agregamos el pixel en el lienzo nuevo
                lienzo_imagen.putpixel((x_sbox, y_sbox), imagen.getpixel((x, y)))

        return lienzo_imagen