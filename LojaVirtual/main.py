from Cliente import Cliente
from Funcionario import Funcionario
from Produto import Produto
from Estoque import Estoque
from Pix import Pix
from EntregaNormal import EntregaNormal
from Compra import Compra

cliente = Cliente("Raphael", 17, 12345678891, "raphael@gmail.com", "1234")
funcionario = Funcionario("Igor", 26, 1234567890, "igor@gmail.com", "5678", 10000)

estoque = Estoque()

notebook = Produto("Notebook", "Um notebook incrível", 2534)
mouse = Produto("Mouse", "Um mouse incrível", 30)

estoque.adicionar(funcionario, notebook)
estoque.adicionar(funcionario, mouse)

print(estoque.mostrar())

cliente.carrinho.adicionar(notebook, 4)
cliente.carrinho.adicionar(mouse, 8)

print(cliente.carrinho.mostrar())

cliente.carrinho.remover(mouse, 8)

print(cliente.carrinho.mostrar())

pagamento = Pix()
entrega = EntregaNormal()
compra = Compra(cliente, pagamento, entrega, estoque)

compra.finalizar()