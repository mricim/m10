def clearList(list):
    res = []
    for val in list:
        if val != None:
            res.append(val)
    return res;


########

def uno():
    list = ["a", "e", "i", "o", "u"]

    num1 = int(input("Modificar (num): "))
    modifica = input("letra: ")
    list[num1] = modifica

    print(list)


def dos():
    list = range(11)

    length = len(list)
    lista = [None] * length
    for pepe in range(length):
        # calculo=(pepe*list[pepe])
        # print("%3d*%3d=%3d"%(pepe,list[pepe],calculo))
        calculo = (7 * list[pepe])
        lista[pepe] = calculo
        print("%3d*%3d=%3d" % (7, list[pepe], calculo))
    print(*lista)


def tres():
    diccionario = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4
    }
    # print(diccionario)
    print("Personas->")
    for key, value in diccionario.items():
        # print (key, value)
        print(key)
    num1 = input("Selecciona uno:")
    print("Nota: " + str(diccionario[num1]))


def cuatro():
    lista1 = ["hola", "juan"]
    lista2 = ["hola2", "juan", "juan2"]

    interseccio = [None] * (len(lista1) + len(lista2))
    interseccioCount = 0
    salidaLista1 = [None] * (len(lista1) + len(lista2))
    salidaLista1Count = 0
    salidaUnio = [None] * (len(lista1) + len(lista2))
    salidaUnioCount = 0

    for i in range(len(lista1)):
        if lista1[i] in lista2:
            interseccio[interseccioCount] = lista1[i]
            interseccioCount += 1
            salidaUnio[salidaUnioCount] = lista1[i]
            salidaUnioCount += 1
            lista2[lista2.index(lista1[i])] = None
            lista1[i] = None
        else:
            salidaLista1[salidaLista1Count] = lista1[i]
            salidaLista1Count += 1
            salidaUnio[salidaUnioCount] = lista1[i]
            salidaUnioCount += 1
            lista1[i] = None

    for a in range(len(lista2)):
        salidaUnio[salidaUnioCount] = lista2[a]
        salidaUnioCount += 1

    interseccio = clearList(interseccio)
    salidaLista1 = clearList(salidaLista1)
    lista2 = clearList(lista2)
    salidaUnio = clearList(salidaUnio)
    print("Intersecció:")
    print(*interseccio)
    print("diferència:")
    print(*salidaLista1)
    print("Lista2:")
    print(*lista2)
    print("Unio:")
    print(*salidaUnio)


# uno()
# dos()
# tres()
cuatro()
