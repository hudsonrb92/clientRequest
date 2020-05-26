class EstabelecimentoSaude():
    def __init__(self, numero_cnes, numero_cnpj, razao_social, nome_fantasia, identificador_endereco, ativo):
        self.__numero_cnes = numero_cnes
        self.__numero_cnpj = numero_cnpj
        self.__razao_social = razao_social
        self.__nome_fantasia = nome_fantasia
        self.__identificador_endereco = identificador_endereco
        self.__ativo = ativo

    @property
    def numero_cnes(self):
        return self.__numero_cnes

    @property
    def numero_cnpj(self):
        return self.__numero_cnpj

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def nome_fantasia(self):
        return self.__nome_fantasia

    @property
    def identificador_endereco(self):
        return self.__identificador_endereco

    @property
    def ativo(self):
        return self.__ativo

    @numero_cnes.setter
    def numero_cnes(self, numero_cnes):
        self.__numero_cnes = numero_cnes

    @numero_cnpj.setter
    def numero_cnpj(self,numero_cnpj):
        self.__numero_cnpj = numero_cnpj

    @razao_social.setter
    def razao_social(self,razao_social):
        self.__razao_social = razao_social

    @nome_fantasia.setter
    def nome_fantasia(self,nome_fantasia):
        self.__nome_fantasia = nome_fantasia

    @identificador_endereco.setter
    def identificador_endereco(self, identificador_endereco):
        self.__identificador_endereco = identificador_endereco

    @ativo.setter
    def ativo(self,ativo):
        self.__ativo = ativo