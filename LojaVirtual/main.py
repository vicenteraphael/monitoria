from Pessoa import *
from Produto import *
from MetodoPagamento import *
from Entrega import *
from Compra import *

cliente = Cliente("Raphael", 17, 12345678891, "raphael@gmail.com", "1234")

notebook = Produto("Notebook", "Um notebook incrível", 2534)
mouse = Produto("Mouse", "Um mouse incrível", 30)
fone = Produto("Fone", "Um fone de ouvido incrível", 18)

cliente.carrinho.adicionar(notebook, 4)
cliente.carrinho.adicionar(mouse, 8)
cliente.carrinho.adicionar(fone, 9)

print(cliente.carrinho)

cliente.carrinho.remover(notebook, 2)
cliente.carrinho.remover(mouse, 8)
cliente.carrinho.remover(fone)

print(cliente.carrinho)

pagamento = Pix()
entrega = EntregaNormal()
compra = Compra(cliente, pagamento, entrega)

compra.finalizar()
