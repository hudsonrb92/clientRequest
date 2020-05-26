class ProfissionalSaude():
    def __init__(self, identificador_pessoa,identificador_tipo_conselho_trabalho,identificador_estado_conselho_trabalho,registro_conselho_trabalho,ativo):
        self.__identificador_pessoa = identificador_pessoa
        self.__identificador_tipo_conselho_trabalho = identificador_tipo_conselho_trabalho
        self.__identificador_estado_conselho_trabalho = identificador_estado_conselho_trabalho
        self.__registro_conselho_trabalho = registro_conselho_trabalho
        self.__ativo = ativo

    @property
    def identificador_pessoa(self):
        return self.__identificador_pessoa

    @property
    def identificador_tipo_conselho_trabalho(self):
        return self.__identificador_tipo_conselho_trabalho

    @property
    def identificador_estado_conselho_trabalho(self):
        return self.__identificador_estado_conselho_trabalho

    @property
    def registro_conselho_trabalho(self):
        return self.__registro_conselho_trabalho

    @property
    def ativo(self):
        return self.__ativo

    @identificador_pessoa.setter
    def identificador_pessoa(self,identificador_pessoa):
        self.__identificador_pessoa = identificador_pessoa

    @identificador_tipo_conselho_trabalho.setter
    def identificador_tipo_conselho_trabalho(self, identificador_tipo_conselho_trabalho):
        self.__identificador_tipo_conselho_trabalho = identificador_tipo_conselho_trabalho

    @identificador_estado_conselho_trabalho.setter
    def identificador_estado_conselho_trabalho(self, identificador_estado_conselho_trabalho):
        self.__identificador_estado_conselho_trabalho = identificador_estado_conselho_trabalho

    @registro_conselho_trabalho.setter
    def registro_conselho_trabalho(self, registro_conselho_trabalho):
        self.__registro_conselho_trabalho = registro_conselho_trabalho

    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo
