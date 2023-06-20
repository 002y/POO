class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def dirigir(self, carro):
        print(f"{self.nome} está dirigindo um {carro.modelo}.")

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo

Pessoa("joão").dirigir(Carro("audi"))
