from Produto import Produto
from Funcionario import Funcionario

class Estoque:
    def __init__(self):
        self.__produtos = []

    @property
    def produtos(self):
        return self.__produtos
    
    def validar_funcionario(self, funcionario):
        if not funcionario.ativo:
            raise PermissionError("Funcionário não pode realizar a operação")
        
    def tem_estoque(self, produto: Produto):
        return produto in self.produtos
    
    def adicionar(self, funcionario: Funcionario, produto: Produto):
        if (not funcionario.ativo):
            print("Funcionário não pode realizar a operação")
            return
        self.produtos.append(produto)

    def aplicar_desconto(self, funcionario: Funcionario, produto: Produto, percentual: float):
        self.validar_funcionario(funcionario)
        produto.preco_unitario *= (1 - percentual)

    def remover(self, funcionario: Funcionario, produto: Produto):
        self.validar_funcionario(funcionario)
        self.produtos.remove(produto)

    def limpar(self, funcionario: Funcionario):
        self.validar_funcionario(funcionario)
        self.__produtos.clear()


    def mostrar(self):
        
        if (len(self.produtos) == 0): return "Estoque vazio"

        desc = ""
        for produto in self.produtos:
            desc += produto.mostrar() + "\n"

        return "Produtos do Estoque:\n" + desc