from model.cliente import cliente
from model.maratona import maratona
from model.fucionario import funcionario

def main():
    funcionario = funcionario ("Pedro")
    cliente = cliente ("Josefino")
    maratona = maratona
    maratona.correr(funcionario)
    maratona.correr(cliente)
if __name__ == "__main__":
    main()
