from pessoa import pessoa

class cliente(pessoa):
    def __init__(self,nome):
        super(cliente, self).__init__(nome)

    def pagar(self):
        print("Cliente pagando de forma Genérica")
