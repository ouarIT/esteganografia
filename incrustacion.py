import PIL.Image as Image
from manejador_bits import llenar_bits


def incrustar_imagen(imagen_rgb: Image, imagen_bn: Image):
    # se usaran los canales rgb de la imagen rgb
    # se usaran los ultimos dos bits de cada canal
    # se guardaran los 6 primeros bit de la imagen bn
    # los primeros dos bits en el canal rojo
    # los segundos dos bits en el canal verde
    # los terceros dos bits en el canal azul

    # se obtienen las dimensiones de la imagen
    width, height = imagen_rgb.size

    # recorremos los pixeles
    for x in range(width):
        for y in range(height):
            # obtenemos el pixel
            pixel = imagen_rgb.getpixel((x, y))
            # obtenemos el pixel de la imagen bn
            pixel_bn = imagen_bn.getpixel((x, y))

            # obtenemos los bits de la imagen bn
            pixel_bn_bin = bin(pixel_bn)[2:]

            if x == 0 and y == 0 and len(pixel_bn_bin) < 8:
                while len(pixel_bn_bin) < 8:
                    pixel_bn_bin = pixel_bn_bin + '0'

            if x == 0 and y == 1 and len(pixel_bn_bin) < 8:
                while len(pixel_bn_bin) < 8:
                    pixel_bn_bin = pixel_bn_bin + '0'

            if len(pixel_bn_bin) < 8:
                pixel_bn_bin = llenar_bits(pixel_bn_bin, 8)

            primer_par = pixel_bn_bin[:2]
            segundo_par = pixel_bn_bin[2:4]
            tercer_par = pixel_bn_bin[4:6]

            # obtenemos los canales de la imagen rgb
            canal_r = bin(pixel[0])[2:]
            canal_g = bin(pixel[1])[2:]
            canal_b = bin(pixel[2])[2:]

            if len(canal_r) < 8:
                canal_r = llenar_bits(canal_r, 8)

            if len(canal_g) < 8:
                canal_g = llenar_bits(canal_g, 8)

            if len(canal_b) < 8:
                canal_b = llenar_bits(canal_b, 8)

            # Sustituimos los ultimos dos bits de cada canal
            canal_r = canal_r[:-2] + primer_par
            canal_g = canal_g[:-2] + segundo_par
            canal_b = canal_b[:-2] + tercer_par

            # hacemos la tupla del pixel
            pixel = (int(canal_r, 2), int(canal_g, 2), int(canal_b, 2))

            # sustituimos el pixel
            imagen_rgb.putpixel((x, y), pixel)

    return imagen_rgb
