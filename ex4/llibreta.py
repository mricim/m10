from ex4.client import Client


class Llibreta:

    def __init__(self):
        self.clientes = []

    def new_client(self, client):
        self.clientes.append(client)

    @classmethod
    def datos_cliente(self):
        nom = input('Introduce el nombre de cliente: ')
        cognom = input('Introduce el apellido de cliente: ')
        telefon = input('Introduce el telefono de cliente: ')
        correu = input('Introduce el correo de cliente: ')
        adreca = input('Introduce la direccion de cliente: ')
        ciutat = input('Introduce la ciudad de cliente: ')
        cliente = Client(nom, cognom, telefon, correu, adreca, ciutat)
        print("id del cliente: ",cliente.id)
        return cliente

    def get_llista_clients(self):
        for cliente in self.clientes:
            print('****************')
            print(cliente)
            print('****************')

    def get_llista_clients_order_by_name(self):
        self.clientes.sort(key=lambda client: client.nom)
        for cliente in self.clientes:
            print('****************')
            print(cliente)
            print('****************')

    def delete_client(self, id):
        clientex = ""
        for cliente in self.clientes:
            if int(cliente.id) == int(id):
                liente = cliente
        if clientex == "":
            print("Este cliente no existe")
        else:
            self.clientes.remove(clientex)

    def clear_list(self):
        self.clientes = []

    def get_id_client(self, id):
        for cliente in self.clientes:
            if int(cliente.id) == int(id):
                return cliente

    def search_by_id(self, id):
        clientex = ""
        for cliente in self.clientes:
            if int(cliente.id) == int(id):
                clientex = cliente
        if clientex == "":
            print("Este cliente no existe")
        else:
            print('****************')
            print(clientex)
            print('****************')

    def search_by_nom(self, nom):
        clientex = ""
        for cliente in self.clientes:
            if cliente.nom == nom:
                clientex = cliente
        if clientex == "":
            print("Este cliente no existe")
        else:
            print('****************')
            print(clientex)
            print('****************')

    def search_by_cognom(self, cognom):
        clientex = ""
        for cliente in self.clientes:
            if cliente.cognom == cognom:
                clientex = cliente
        if clientex == "":
            print("Este cliente no existe")
        else:
            print('****************')
            print(clientex)
            print('****************')
