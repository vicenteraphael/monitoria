class Produto:
    def __init__(self, nome, descricao, preco_unitario):
        self.nome = nome
        self.descricao = descricao
        self.preco_unitario = preco_unitario

    def __repr__(self):
        return f"Produto: {self.nome}, R${self.preco_unitario}"