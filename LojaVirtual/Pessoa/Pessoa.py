from abc import ABC

class Pessoa(ABC):
    def __init__(self, nome, idade, cpf, email, senha):
        self._nome = nome
        self._idade = idade
        self.__cpf = cpf
        self._email = email
        self.__senha = senha

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha