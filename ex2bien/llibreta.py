import datetime
from ex2bien.client import Client
# Store the next available id for all new notes
class Llibreta:
    '''Represent a collection of notes that can be tagged,
    modified, and searched.'''

    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.customers = []

    def new_client(self,client):
        '''Create a new client and add it to the list.'''
        self.customers.append(client)
    
    @classmethod
    def datos_cliente(self):
        nom = input('Introduce el nombre de cliente: ')
        cognom = input('Introduce el apellido de cliente: ')
        telefon = input('Introduce el telefono de cliente: ')
        correu = input('Introduce el correo de cliente: ')
        adreca = input('Introduce la direccion de cliente: ')
        ciutat = input('Introduce la ciudad de cliente: ')
        cliente  = Client(nom,cognom,telefon,correu,adreca,ciutat)
        return cliente


    def get_llista_clients(self):
        for c in self.customers:
            print('****************')
            print(c)
            print('****************')

    def delete_client(self,id):
        for c in self.customers:
            if int(c.id) == int(id):
                self.customers.remove(c)

    
    def clear_list(self):
        self.customers = []
    
    def get_id_client(self,id):
        for c in self.customers:
            if int(c.id) == int(id):
                return c 
    
    def search_by_id(self,id ):
        for c in self.customers:
            if int(c.id) == int(id):
                print('****************')
                print(c)
                print('****************')


    
    def search_by_nom(self,nom ):
        for c in self.customers:
            if c.nom == nom:
                print('****************')
                print(c) 
                print('****************')
    
    def search_by_cognom(self,cognom ):
        for c in self.customers:
            if c.cognom == cognom:
                print('****************')
                print(c)
                print('****************')