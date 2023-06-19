aboytes_s_box = (
    (0, 228, 211, 223, 18, 141, 12, 111, 45, 62, 129, 126, 30, 91, 93, 21),
    (114, 92, 218, 68, 214, 117, 64, 13, 16, 188, 78, 246, 144, 155, 115, 234),
    (207, 221, 69, 150, 72, 176, 105, 170, 209, 174, 97, 100, 201, 160, 103, 168),
    (29, 219, 146, 75, 249, 113, 65, 3, 112, 74, 241, 134, 210, 130, 222, 26),
    (36, 197, 9, 226, 28, 204, 14, 39, 180, 152, 81, 235, 82, 225, 104, 59),
    (88, 229, 242, 143, 2, 67, 102, 123, 122, 172, 173, 119, 247, 58, 161, 184),
    (24, 128, 61, 6, 56, 4, 8, 7, 106, 83, 202, 110, 120, 22, 165, 179),
    (33, 85, 86, 131, 37, 183, 94, 167, 48, 66, 227, 163, 138, 77, 215, 136),
    (90, 32, 53, 148, 162, 51, 220, 47, 54, 159, 151, 195, 27, 248, 233, 99),
    (76, 178, 157, 181, 31, 137, 87, 231, 35, 199, 118, 25, 251, 205, 182, 95),
    (107, 156, 200, 101, 1, 244, 166, 132, 187, 5, 254, 19, 40, 255, 79, 127),
    (142, 193, 140, 55, 149, 63, 239, 50, 240, 125, 171, 116, 206, 213, 42, 189),
    (60, 73, 41, 109, 208, 43, 15, 121, 108, 70, 10, 250, 20, 23, 185, 98),
    (11, 145, 196, 34, 80, 245, 153, 243, 253, 175, 191, 238, 203, 224, 124, 17),
    (186, 230, 57, 52, 164, 135, 44, 154, 71, 236, 38, 232, 216, 147, 177, 192),
    (217, 237, 46, 169, 158, 84, 198, 190, 212, 96, 89, 49, 194, 139, 252, 133)
)

aboytes_inversa_s_box = (
    (0, 164, 84, 55, 101, 169, 99, 103, 102, 66, 202, 208, 6, 23, 70, 198),
    (24, 223, 4, 171, 204, 15, 109, 205, 96, 155, 63, 140, 68, 48, 12, 148),
    (129, 112, 211, 152, 64, 116, 234, 71, 172, 194, 190, 197, 230, 8, 242, 135),
    (120, 251, 183, 133, 227, 130, 136, 179, 100, 226, 93, 79, 192, 98, 9, 181),
    (22, 54, 121, 85, 19, 34, 201, 232, 36, 193, 57, 51, 144, 125, 26, 174),
    (212, 74, 76, 105, 245, 113, 114, 150, 80, 250, 128, 13, 17, 14, 118, 159),
    (249, 42, 207, 143, 43, 163, 86, 46, 78, 38, 104, 160, 200, 195, 107, 7),
    (56, 53, 16, 30, 187, 21, 154, 91, 108, 199, 88, 87, 222, 185, 11, 175),
    (97, 10, 61, 115, 167, 255, 59, 229, 127, 149, 124, 253, 178, 5, 176, 83),
    (28, 209, 50, 237, 131, 180, 35, 138, 73, 214, 231, 29, 161, 146, 244, 137),
    (45, 94, 132, 123, 228, 110, 166, 119, 47, 243, 39, 186, 89, 90, 41, 217),
    (37, 238, 145, 111, 72, 147, 158, 117, 95, 206, 224, 168, 25, 191, 247, 218),
    (239, 177, 252, 139, 210, 65, 246, 153, 162, 44, 106, 220, 69, 157, 188, 32),
    (196, 40, 60, 2, 248, 189, 20, 126, 236, 240, 18, 49, 134, 33, 62, 3),
    (221, 77, 67, 122, 1, 81, 225, 151, 235, 142, 31, 75, 233, 241, 219, 182),
    (184, 58, 82, 215, 165, 213, 27, 92, 141, 52, 203, 156, 254, 216, 170, 173)
)

rijndael_s_box = (
    (99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118),
    (202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 192),
    (183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21),
    (4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117),
    (9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132),
    (83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207),
    (208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168),
    (81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210),
    (205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115),
    (96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219),
    (224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121),
    (231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8),
    (186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138),
    (112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158),
    (225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223),
    (140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22)
)

rijndael_inversa_s_box = (
    (82, 9, 106, 213, 48, 54, 165, 56, 191, 64, 163, 158, 129, 243, 215, 251),
    (124, 227, 57, 130, 155, 47, 255, 135, 52, 142, 67, 68, 196, 222, 233, 203),
    (84, 123, 148, 50, 166, 194, 35, 61, 238, 76, 149, 11, 66, 250, 195, 78),
    (8, 46, 161, 102, 40, 217, 36, 178, 118, 91, 162, 73, 109, 139, 209, 37),
    (114, 248, 246, 100, 134, 104, 152, 22, 212, 164, 92, 204, 93, 101, 182, 146),
    (108, 112, 72, 80, 253, 237, 185, 218, 94, 21, 70, 87, 167, 141, 157, 132),
    (144, 216, 171, 0, 140, 188, 211, 10, 247, 228, 88, 5, 184, 179, 69, 6),
    (208, 44, 30, 143, 202, 63, 15, 2, 193, 175, 189, 3, 1, 19, 138, 107),
    (58, 145, 17, 65, 79, 103, 220, 234, 151, 242, 207, 206, 240, 180, 230, 115),
    (150, 172, 116, 34, 231, 173, 53, 133, 226, 249, 55, 232, 28, 117, 223, 110),
    (71, 241, 26, 113, 29, 41, 197, 137, 111, 183, 98, 14, 170, 24, 190, 27),
    (252, 86, 62, 75, 198, 210, 121, 32, 154, 219, 192, 254, 120, 205, 90, 244),
    (31, 221, 168, 51, 136, 7, 199, 49, 177, 18, 16, 89, 39, 128, 236, 95),
    (96, 81, 127, 169, 25, 181, 74, 13, 45, 229, 122, 159, 147, 201, 156, 239),
    (160, 224, 59, 77, 174, 42, 245, 176, 200, 235, 187, 60, 131, 83, 153, 97),
    (23, 43, 4, 126, 186, 119, 214, 38, 225, 105, 20, 99, 85, 33, 12, 125)
)


def calcular_inversa_s_box(box):
    inversa = [[0] * len(box) for _ in range(len(box))]

    for fila in range(len(box)):
        for columna in range(len(box[fila])):
            # obtenemos el valor de la caja
            valor = box[fila][columna]

            fila_valor = valor // 16  # obtenemos la fila del valor
            columna_valor = valor % 16  # obtenemos la columna del valor

            # ingresamos el valor en la fila y columna correspondiente

            inversa[fila_valor][columna_valor] = fila*16 + columna

    return tuple(tuple(fila) for fila in inversa)
