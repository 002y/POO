from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('macbook', 10000)
p2 = Produto('pc gamer', 8000)
p3 = Produto('livro', 30)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.lista_produto()
print(carrinho.soma_total())
