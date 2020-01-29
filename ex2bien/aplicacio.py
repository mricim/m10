#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-
import time
from ex2bien.menu import Menu
from ex2bien.llibreta import Llibreta
from ex2bien.client import Client

menu = Menu()
llibreta = Llibreta()
opcio = menu.get_principal()

c1 = Client("pepe","perico","43543534534","asdasda@gmail.com","asdasdasdas","BCN")
c2 = Client("pepe2","perico2","43543534534","asdasda@gmail.com","asdasdasdas","BCN")
c3 = Client("pepe3","perico3","43543534534","asdasda@gmail.com","asdasdasdas","BCN")
c4 = Client("pepe4","perico4","43543534534","asdasda@gmail.com","asdasdasdas","BCN")

llibreta.new_client(c1)
llibreta.new_client(c2)
llibreta.new_client(c3)
llibreta.new_client(c4)


# Menu options
while opcio != 5:
    if opcio == 1:
        cliente = Llibreta.datos_cliente()
        llibreta.new_client(cliente)
        time.sleep(2)
        opcio = menu.get_principal()
    elif opcio == 2:
        id_cli = input('Introduce el id del cliente que quieres borrar: \n')
        llibreta.delete_client(id_cli)
        time.sleep(2)
        opcio = menu.get_principal()
    elif opcio == 3:
        # Menu de consulta
        opcio_consulta = menu.get_consulta()
        if opcio_consulta == 1:
            id_cli = input(
                'Introduce el id del cliente que quieres buscar: \n')
            llibreta.search_by_id(id_cli)
        elif opcio_consulta == 2:
            nom = input(
                'Introduce el nombre del cliente que quieres buscar : \n')
            llibreta.search_by_nom(nom)
        elif opcio_consulta == 3:
            cognom = input(
                'Introduce el apellido del cliente que quieres buscar : \n')
            llibreta.search_by_nom(cognom)
        elif opcio_consulta == 4:
            llibreta.get_llista_clients()
        elif opcio_consulta == 5:
            llibreta.get_llista_clients()
        elif opcio_consulta == 6:
            opcio = menu.get_principal()
    elif opcio == 4:
        id_cli = input('Introduce el id del cliente que quieres modificar: \n')
        campo = input('Introduce el nombre del campo que quieres modificar: ')
        nuevo_valor = input('Introduce el nuevo valor del campo: ')
        cliente = llibreta.get_id_client(id_cli)
        setattr(cliente, campo, nuevo_valor)
        time.sleep(1)
        opcio = menu.get_principal()
    elif opcio == 5:
        break
