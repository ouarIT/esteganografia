import arnold_cat_map
from arnold_cat_map import arnold_cat_map as acm
from arnold_cat_map import arnold_cat_map_iterador as ami
import s_boxes
from map_sbox import mapeo as m

path = 'C:/Users/ouarit/Documents/esteganografia/1.jpg'

counter, counter_min, imagen_menor_correlacion = acm(path)

imagen_menor_correlacion.show()

# aqui se agrega la informacion a la imagen

# aqui se hace el mapeo de la imagen

imagen_menor_correlacion = m(imagen_menor_correlacion, s_boxes.rijndael_s_box)
imagen_menor_correlacion.show()

# mapeo doble
imagen_menor_correlacion = m(imagen_menor_correlacion, s_boxes.aboytes_s_box)
imagen_menor_correlacion.show()

# desmapeo doble
imagen_menor_correlacion = m(imagen_menor_correlacion, s_boxes.aboytes_inversa_s_box)
imagen_menor_correlacion.show()

# aqui se hace el desmapeo de la imagen

imagen_menor_correlacion = m(imagen_menor_correlacion, s_boxes.rijndael_inversa_s_box)
imagen_menor_correlacion.show()

# se iteran las veces faltantes para volver a la imagen original

imagen_menor_correlacion = ami(imagen_menor_correlacion, counter-counter_min)
imagen_menor_correlacion.show()