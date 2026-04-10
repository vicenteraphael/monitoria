import Pessoa.Pessoa as Pessoa, Carrinho.Carrinho as Carrinho

class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf, email, senha):
        super().__init__(nome, idade, cpf, email, senha)
        self.carrinho = Carrinho()