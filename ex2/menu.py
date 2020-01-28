import sys
from datetime import time

from ex2.client import Client
from ex2.libreta import Libreta


class Menu:
    def __init__(self):
        self.choices_menu = {
            "1": Client.new_client(self),
            "2": Libreta.remove_client(self),
            "3": self.get_consulta,
            "4": Client.modifique_client(),
            "5": self.quit
        }
        self.choices_consulta = {
            #               "1": self.search_client_id,
            #               "2": self.search_client_name,
            #               "3": self.search_client_last_name,
            "4": Libreta.get_llista_clients(self),
            #               "5": self.list_clients_name,
            "6": self.quit
        }

    def display_menu(self):
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

    def display_menu_consulta(self):
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
\t6. Quit
""")

    def get_principal(self):
        while True:
            self.display_menu()
            option = str(input("Enter an option: "))
            action = self.choices_menu.get(option)
            if action:
                action()
                time.sleep(5)
            else:
                print("{0} is not a valid choice".format(option))

    def get_consulta(self):
        while True:
            self.display_menu_consulta()
            option = input("Enter an option: ")
            action = self.choices_consulta.get(option)
            if action:
                action()
                time.sleep(5)
            else:
                print("{0} is not a valid choice".format(option))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(
                note.id, note.tags, note.memo))

    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)

#    if __name__ == "__main__":
#        Menu().get_principal()
