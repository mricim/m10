from ex2 import libreta
from ex2.libreta import last_id, Libreta


class Client:
    id = ""
    name = ""
    cognom = ""
    telefon = ""
    correu = ""
    adreca = ""
    ciutat = ""

    def __init__(self):
        self.id = 1 + last_id

    def new_client(self, name, cognom, telefon, correu, adreca, ciutat):
        self.name = name
        self.cognom = cognom
        self.telefon = telefon
        self.correu = correu
        self.adreca = adreca
        self.ciutat = ciutat
        Libreta.afegir_client(self)
