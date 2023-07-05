import s_boxes
from PIL.Image import open as load_pic
import redimensionador
import map_sbox

path = 'C:/Users/ouarit/Documents/esteganografia/2.jpg'

imagen_a_ocultar = load_pic('C:/Users/ouarit/Documents/esteganografia/1.jpg')
imagen_encubridora = load_pic(path)

imagen_encubridora, imagen_a_ocultar = redimensionador.redimensionar(imagen_encubridora, imagen_a_ocultar)

imagen_a_ocultar.show()

imagen_a_ocultar = map_sbox.mapeo_coordenadas(imagen_a_ocultar, s_boxes.aboytes_s_box)
imagen_a_ocultar.show()
imagen_a_ocultar = map_sbox.mapeo_coordenadas(imagen_a_ocultar, s_boxes.aboytes_inversa_s_box)
imagen_a_ocultar.show()
