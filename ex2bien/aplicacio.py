import time
from ex2bien.menu import Menu
from ex2bien.llibreta import Llibreta
from ex2bien.client import Client

menu = Menu()
libreta = Llibreta()
opcion = menu.get_principal()

cliente1 = Client("1cosa", "madrazo1", "11111", "asd@gmail.com", "asd", "bcn")
cliente2 = Client("2cosa", "madrazo2", "22222", "sdf@gmail.com", "sdf", "alc")
cliente3 = Client("cosa3", "madrazo3", "33333", "dfg@gmail.com", "dfg", "md")
cliente4 = Client("4cosa", "madrazo4", "33333", "fgh@gmail.com", "fgh", "cc")

libreta.new_client(cliente1)
libreta.new_client(cliente2)
libreta.new_client(cliente3)
libreta.new_client(cliente4)

while opcion != 5:
    if opcion == 1:
        libreta.new_client(Llibreta.datos_cliente())
    elif opcion == 2:
        libreta.delete_client(input('Introduce el id del cliente que quieres borrar: '))
    elif opcion == 3:
        # Menu consulta
        opcio_consulta = menu.get_consulta()
        while opcio_consulta != 6:
            if opcio_consulta == 1:
                libreta.search_by_id(input('Introduce el id del cliente que quieres buscar: '))
            elif opcio_consulta == 2:
                libreta.search_by_nom(input('Introduce el nombre del cliente que quieres buscar : '))
            elif opcio_consulta == 3:
                libreta.search_by_nom(input('Introduce el apellido del cliente que quieres buscar : '))
            elif opcio_consulta == 4:
                libreta.get_llista_clients()
            elif opcio_consulta == 5:
                libreta.get_llista_clients_order_by_name()
            elif opcio_consulta == 6:
                break
                # Vuelve al menu principal
            time.sleep(10)
            opcio_consulta = menu.get_consulta()
    elif opcion == 4:
        id_cli = input('Introduce el id del cliente que quieres modificar: ')
        campo = input('Introduce el nombre del campo que quieres modificar: ')
        nuevo_valor = input('Introduce el nuevo valor del campo: ')
        setattr(libreta.get_id_client(id_cli), campo, nuevo_valor)
    elif opcion == 5:
        break
    print("------------------------------------------------")
    time.sleep(10)
    print('\n' * 5)  # prints 80 line breaks
    opcion = menu.get_principal()
