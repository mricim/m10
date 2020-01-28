last_id = 0;

class Libreta:


    lista_client = []
    def __init__(self):
        self.lista_client = []


    def afegir_client(self,client):
        self.lista_client.append(client)
        last_id = client.id

    def remove_client(self,id):
        for client in self.lista_client:
            if str(client.id) == str(id):
                return client
        return None
    def cerca_per_id(self,id):
        for client in self.lista_client:
            if str(client.id) == str(id):
                return client
        return None
    def cerca_per_nom(self,nom):
        for client in self.lista_client:
            if str(client.nom) == str(nom):
                return client
        return None
    def cerca_per_cognom(self,cognom):
        for client in self.lista_client:
            if str(client.cognom) == str(cognom):
                return client
        return None