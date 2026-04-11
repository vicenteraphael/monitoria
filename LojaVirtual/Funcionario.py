from Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, email, senha, salario):
        super().__init__(nome, idade, cpf, email, senha)
        self._salario = salario
        self._ativo = True

    def desativar(self):
        self.ativo = False

    def ativar(self):
        self.ativo = True
    