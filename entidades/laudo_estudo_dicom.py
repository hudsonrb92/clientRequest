class LaudoEstudoDicom():
    def __init__(self, identificador_estudo_dicom, data_hora_emissao, identificador_profissional_saude, texto, situacao,
                 situacao_envio_his):
        self.__identificador_estudo_dicom = identificador_estudo_dicom
        self.__data_hora_emissao = data_hora_emissao
        self.__identificador_profissional_saude = identificador_profissional_saude
        self.__texto = texto
        self.__situacao = situacao
        self.__situacao_envio_his = situacao_envio_his

    @property
    def identificador_estudo_dicom(self):
        return self.__identificador_estudo_dicom

    @property
    def data_hora_emissao(self):
        return self.__data_hora_emissao

    @property
    def identificador_profissional_saude(self):
        return self.__identificador_profissional_saude

    @property
    def texto(self):
        return self.__texto

    @property
    def situacao(self):
        return self.__situacao

    @property
    def situacao_envio_his(self):
        return self.__situacao_envio_his

    @identificador_estudo_dicom.setter
    def identificador_estudo_dicom(self, identificador_estudo_dicom):
        self.__identificador_estudo_dicom = identificador_estudo_dicom

    @data_hora_emissao.setter
    def data_hora_emissao(self, data_hora_emissao):
        self.__data_hora_emissao = data_hora_emissao

    @identificador_profissional_saude.setter
    def identificador_profissional_saude(self, identificador_profissional_saude):
        self.__identificador_profissional_saude = identificador_profissional_saude

    @texto.setter
    def texto(self, texto):
        self.__texto = texto

    @situacao.setter
    def situacao(self, situacao):
        self.__situacao = situacao

    @situacao_envio_his.setter
    def situacao_envio_his(self, situacao_envio_his):
        self.__situacao_envio_his = situacao_envio_his
