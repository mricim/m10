class Menu:

    def get_principal(self):
        print("""
        Menu principal
        =========================================
        Seleciona una opcion y presiona "Intro"
        =========================================
        \t1. Añadir cliente
        \t2. Elimiar cliente
        \t3. Consultar cliente
        \t4. Modificar un campo de un cliente
        \t5. Quit""")

        opcion = int(input('\nEscoge una opcion: '))
        while opcion < 1 or opcion > 5:
            opcion = int(input('\nEscoge una opcion (entre 1 y 5): '))
        return opcion

    def get_consulta(self):
        print("""
        Menu consuta
        =========================================
        Seleciona una opcion y presiona "Intro"
        =========================================
        \t1. Buscar cliente por Id
        \t2. Buscar cliente por nombre
        \t3. Buscar cliente por apellido
        \t4. Listar todos los clientes
        \t5. Listar todos los clientes por nombre
        \t6. Quit""")

        opcion = int(input('\nEscoge una opcion: '))
        while opcion < 1 or opcion > 6:
            opcion = int(input('\nEscoge una opcion (entre 1 y 6): '))
        return opcion
