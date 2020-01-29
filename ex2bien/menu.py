#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-
class Menu:
    def get_principal(self):
        # Muestra el menu por pantalla y lee una opcion de teclado, que es el
        # resultado devuelto.
        # La funcion se asegura de que la opcion leida este entre 0 y 8.
        print('*** MAIN MENU ***')
        print('===================================')
        print('Seleccioni una opció i premi Intro')
        print('===================================')
        print('1) Afegir client')
        print('2) Eliminar client')
        print('3) Consultar client')
        print('4) Modificar un camp')
        print('5) Salir')

        opcion = int(input('Escoge opcion: '))
        while opcion < 1 or opcion > 5:
            opcion = input(input('Escoge opcion (entre 1 y 5): '))
        return opcion

    def get_consulta(self):
        # Muestra el menu por pantalla y lee una opcion de teclado, que es el
        # resultado devuelto.
        # La funcion se asegura de que la opcion leida este entre 0 y 8.
        print('*** MENU CONSULTA ***')
        print('===================================')
        print('Seleccioni una opció i premi Intro')
        print('===================================')
        print('1) Cercar client per identificador')
        print('2) Cercar client per nom')
        print('3) Cercar client per Cognom')
        print('4) Llista tots els clients')
        print('5) Llista tots els clients per Nom (*)')
        print('6) Enrere')

        opcion = int(input('Escoge opcion: '))
        while opcion < 1 or opcion > 6:
            opcion = input(input('Escoge opcion (entre 1 y 6): '))
        return opcion
