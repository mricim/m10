from ex2 import libreta
from ex2.libreta import last_id, Libreta


class Client(object):
    id = ""
    name = ""
    cognom = ""
    telefon = ""
    correu = ""
    adreca = ""
    ciutat = ""

    def __init__(self, name, cognom, telefon, correu, adreca, ciutat):
        self.id = 1 + last_id
        self.name = name
        self.cognom = cognom
        self.telefon = telefon
        self.correu = correu
        self.adreca = adreca
        self.ciutat = ciutat

    def new_client(self):
        client = Client(input("Name: "), input("cognom: "), input("telefon: "), input("correu: "), input("adreca: "), input("ciutat: "))
        Libreta.afegir_client(client)

    @classmethod
    def modifique_client(cls):
        cliente=Libreta.cerca_per_id()

        cliente.name=input("Name: ")
        cliente.cognom = input("cognom: ")
        cliente.telefon = input("telefon: ")
        cliente.correu = input("correu: ")
        cliente.adreca = input("adreca: ")
        cliente.ciutat = input("ciutat: ")
        pass
