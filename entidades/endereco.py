class Endereco():
    def __init__(self, identificador_tipo_endereco, logradouro, ativo):
        self.__identificador_tipo_endereco = identificador_tipo_endereco
        self.__logradouro = logradouro
        self.__ativo = ativo

    @property
    def identificador_tipo_endereco(self):
        return self.__identificador_tipo_endereco

    @property
    def logradouro(self):
        return self.__logradouro

    @property
    def ativo(self):
        return self.__ativo

    @identificador_tipo_endereco.setter
    def identificador_tipo_endereco(self, identificador_tipo_endereco):
        self.__identificador_tipo_endereco = identificador_tipo_endereco

    @logradouro.setter
    def logradouro(self, logradouro):
        self.__logradouro = logradouro

    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo
