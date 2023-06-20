'''
public, protected, private
_ privado/protected (public _)
__ privado (_NOMECLASSE__nomeatributo)
'''
class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

print('amigos: ')
amigos = BaseDeDados()
amigos.inserir_cliente(1, 'roberth')
amigos.inserir_cliente(2, 'joão')
amigos.inserir_cliente(3, 'malu')
amigos.inserir_cliente(4, 'clarinha')
amigos.__dados = 'amo vcs'
print(amigos._BaseDeDados__dados)
print(amigos.__dados)

print()
print('familia: ')
familia = BaseDeDados()
familia.inserir_cliente(1, 'mãe')
familia.inserir_cliente(2, 'pai')
familia.inserir_cliente(3, 'emily')
print(familia.lista_clientes())
print(familia._BaseDeDados__dados)
