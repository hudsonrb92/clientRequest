class Sexo():
    def __init__(self, descricao, sigla, ativo):
        self.__descricao = descricao
        self.__sigla = sigla
        self.__ativo = ativo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def sigla(self):
        return self.__sigla

    @sigla.setter
    def sigla(self, sigla):
        self.__sigla = sigla

    @property
    def ativo(self):
        return self.__ativo

    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo