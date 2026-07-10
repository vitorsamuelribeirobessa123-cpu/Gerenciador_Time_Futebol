from abc import ABC, abstractmethod

class Membro(ABC):

    def __init__(self, nome, idade, salario):
        self.__nome = nome
        self.__idade = idade
        self.__salario = salario

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario

    @abstractmethod
    def calcular_salario(self):
        pass