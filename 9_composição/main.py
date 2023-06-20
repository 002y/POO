from classes import Cliente, Endereco

cliente1 = Cliente('Roberth', 16)
cliente1.insere_endereco('janaúba', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
print()

cliente2 = Cliente('malu', 16)
cliente2.insere_endereco('moc', 'MG')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

