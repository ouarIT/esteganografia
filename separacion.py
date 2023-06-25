import PIL.Image as Image
from manejador_bits import llenar_bits


def separar_imagen(imagen: Image):
    width, height = imagen.size
    # creamos el lienzo para obtener la imagen oculta en blanco y negro
    lienzo_nuevo = Image.new("L", (width, height))

    for x in range(width):
        for y in range(height):
            pixel = imagen.getpixel((x, y))
            # pasamos a binario y llenamos para tener un formato de 8

            r = llenar_bits(bin(pixel[0])[2:], 8)
            g = llenar_bits(bin(pixel[1])[2:], 8)
            b = llenar_bits(bin(pixel[2])[2:], 8)

            # creamos el nuevo pixel
            newPixel = r[-2:]+g[-2:]+b[-2:]+'00'

            lienzo_nuevo.putpixel((x, y), int(newPixel, 2))

    return lienzo_nuevo


def obtener_bits(imagen: Image):
    pixel1 = imagen.getpixel((0, 0))
    print('pixel', (bin(pixel1)))

    pixel2 = imagen.getpixel((0, 1))
    print('pixel', (bin(pixel2)))
