import s_boxes
from map_sbox import mapeo as m
from separacion import separar_imagen as si
from separacion import obtener_diferencia as od
from PIL.Image import open as load_pic
import PIL.Image as Image
from arnold_cat_map import arnold_cat_map_iterador as ami

def desencriptador_str(path: str):
    # carga de imagen
    imagen = load_pic(path)
    imagen = si(imagen)

    

    imagen = m(imagen, s_boxes.aboytes_inversa_s_box)
    imagen = m(imagen, s_boxes.rijndael_inversa_s_box)
    
    imagen.show()
    # se iteran las veces faltantes para volver a la imagen original

    diferencia = od(imagen)
    

    imagen = ami(imagen, diferencia)
    imagen.show()

def checador_bits(imagen):
    pixel1 = imagen.getpixel((0,0))
    pixel2 = imagen.getpixel((0,1))

    print('canal r', bin(pixel1[0]), 'canal g', bin(pixel1[1]), 'canal b', bin(pixel1[2]))
    print('canal r', bin(pixel2[0]), 'canal g', bin(pixel2[1]), 'canal b', bin(pixel2[2]))

if __name__ == '__main__':
    path = 'C:/Users/ouarit/Documents/esteganografia/imagen_esteganografiada_21-06-2023_16-07-17.jpg'
    desencriptador_str(path)