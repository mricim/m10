def calcularDni():
    diccionario = {
        0: "T",
        1: "R",
        2: "W",
        3: "A",
        4: "G",
        5: "M",
        6: "I",
        7: "F",
        8: "P",
        9: "D",
        10: "X",
        11: "B",
        12: "N",
        13: "J",
        14: "Z",
        15: "S",
        16: "Q",
        17: "V",
        18: "H",
        19: "L",
        20: "C",
        21: "K",
        22: "E",
    }
    dni=input("Dni:")
    numero=dni[:-1]
    letra=dni[-1:]
    #print(numero)
    #print(letra)
    resultado=int(numero)%23
    if diccionario[resultado]==letra.upper():
        print("Correcto")
    else:
        print("MAL")
calcularDni()