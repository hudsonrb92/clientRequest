class PerfilUsuarioEstabelecimentoSaude():
    def __init__(self, identificador_perfil, identificador_estabelecimento_saude, data_inicial):
        self.__identificador_perfil = identificador_perfil
        self.__identificador_estabelecimento_saude = identificador_estabelecimento_saude
        self.__data_inicial = data_inicial


    @property
    def identificador_perfil(self):
        return self.__identificador_perfil

    @identificador_perfil.setter
    def identificador_perfil(self, identificador_perfil):
        self.__identificador_perfil = identificador_perfil

    @property
    def identificador_estabelecimento_saude(self):
        return self.__identificador_estabelecimento_saude

    @identificador_estabelecimento_saude.setter
    def identificador_estabelecimento_saude(self, identificador_estabelecimento_saude):
        self.__identificador_estabelecimento_saude = identificador_estabelecimento_saude

    @property
    def data_inicial(self):
        return self.__data_inicial

    @data_inicial.setter
    def data_inicial(self, data_inicial):
        self.__data_inicial = data_inicial