last_id = 0;


class Libreta(object):
    lista_client = []

    def __init__(self):
        self.lista_client = []

    def afegir_client(client):
        Libreta.lista_client.append(client)
        last_id = client.id

    def remove_client(self, id):
        self.lista_client.remove(id)
        return None

    def cerca_per_id(self, id):
        id = input("Id del cliente: ")
        client = next((x for x in Libreta.lista_client if x.id == id), None)
        return client

    def cerca_per_nom(self, nom):
        for client in self.lista_client:
            if str(client.nom) == str(nom):
                return client
        return None

    def cerca_per_cognom(self, cognom):
        for client in self.lista_client:
            if str(client.cognom) == str(cognom):
                return client
        return None

    def get_llista_clients(self):
        if not Libreta.lista_client:
            print(*Libreta.lista_client)
        else:
            print("\n\nNot clients")
