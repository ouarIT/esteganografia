from arnold_cat_map import arnold_cat_map as acm
import s_boxes
from map_sbox import mapeo as m
from formateo import incrustacion as inc
from PIL.Image import open as load_pic
from incrustacion import incrustar_imagen as ii
from datetime import datetime
from desencriptador import desencriptador


path = 'C:/Users/ouarit/Documents/esteganografia/2.jpg'

imagen_a_ocultar = load_pic('C:/Users/ouarit/Documents/esteganografia/1.jpg')
imagen_encubridora = load_pic(path)

# si es mayor se hace un resize de la imagen encubridora
imagen_encubridora = imagen_encubridora.resize(
    (imagen_a_ocultar.width, imagen_a_ocultar.height))

diferencia, imagen_menor_correlacion = acm(imagen_a_ocultar)

# aqui se agrega la informacion a la imagen
imagen_menor_correlacion = inc(imagen_menor_correlacion, diferencia)

# aqui se hace el mapeo de la imagen
imagen_menor_correlacion = m(imagen_menor_correlacion, s_boxes.rijndael_s_box)

# mapeo doble
imagen_menor_correlacion = m(imagen_menor_correlacion, s_boxes.aboytes_s_box)

# incrustacion de la imagen
imagen_menor_correlacion = ii(imagen_encubridora, imagen_menor_correlacion)

# crear nombre para guardar la imagen, agregando la hora y fecha
formato = ''
for i in path[::-1]:
    if i == '.':
        formato += i
        break
    formato += i


nombre_imagen = 'imagen_esteganografiada_' + \
    str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S")) + formato[::-1]

# guardar la imagen
imagen_menor_correlacion.save(nombre_imagen)
