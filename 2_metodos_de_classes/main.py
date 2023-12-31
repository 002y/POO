
class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

#linha 18 e 19 fazem a mesma coisa
p1 = Pessoa.por_ano_nascimento('Roberth', 2008)
#p1 = Pessoa('Roberth', 15)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
