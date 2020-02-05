last_id = 0
class Client:
    def __init__(self,nom,cognom,telefon,correu,adreca,ciutat):
        '''
        Client constructor
        '''
        global last_id
        last_id = last_id +1
        self.id = last_id
        self.nom = nom
        self.cognom = cognom
        self.telefon = telefon
        self.correu = correu
        self.adreca = adreca
        self.ciutat = ciutat

    def __str__(self):
        return 'ID: {0}\nNombre: {1}\nApellido: {2}\nTelefono: {3}\nCorreo: {4}\nAdreca: {5}\nCiutat: {6}' \
            .format(self.id, self.nom, self.cognom, self.telefon,self.correu,self.adreca,self.ciutat)

