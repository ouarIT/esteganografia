
imagen_menor_correlacion = m(imagen_menor_correlacion, s_boxes.aboytes_inversa_s_box)
imagen_menor_correlacion = m(imagen_menor_correlacion, s_boxes.rijndael_inversa_s_box)
# se iteran las veces faltantes para volver a la imagen original

imagen_menor_correlacion = ami(imagen_menor_correlacion, diferencia)
imagen_menor_correlacion.show()