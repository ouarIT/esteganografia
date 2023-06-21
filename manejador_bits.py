def llenar_bits(bits: str, cantidad: int):
    # llenamos los bits con 0 a la izquierda
    while len(bits) < cantidad:
        bits = '0' + bits

    return bits