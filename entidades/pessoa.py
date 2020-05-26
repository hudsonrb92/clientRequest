class Pessoa():
    def __init__(self, nome, ativa):
        self.__nome = nome
        self.__ativa = ativa

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def ativa(self):
        return self.__ativa

    @ativa.setter
    def ativa(self, ativa):
        self.__ativa = ativa