class AnotacaoEstudoDicom():
    def __init__(self, identificador_estudo_dicom, data_hora_registro, identificador_profissional_saude, texto, origem):
        self.__identificador_estudo_dicom = identificador_estudo_dicom
        self.__data_hora_registro = data_hora_registro
        self.__identificador_profissional_saude = identificador_profissional_saude
        self.__texto = texto
        self.__origem = origem

    @property
    def identificador_estudo_dicom(self):
        return self.__identificador_estudo_dicom

    @property
    def data_hora_registro(self):
        return self.__data_hora_registro

    @property
    def identificador_profissional_saude(self):
        return self.__identificador_profissional_saude

    @property
    def texto(self):
        return self.__texto

    @property
    def origem(self):
        return self.__origem

    @identificador_estudo_dicom.setter
    def identificador_estudo_dicom(self,identificador_estudo_dicom):
        self.__identificador_estudo_dicom = identificador_estudo_dicom

    @data_hora_registro.setter
    def data_hora_registro(self,data_hora_registro):
        self.__data_hora_registro = data_hora_registro

    @identificador_profissional_saude.setter
    def identificador_profissional_saude(self, identificador_profissional_saude):
        self.__identificador_profissional_saude = identificador_profissional_saude

    @texto.setter
    def texto(self,texto):
        self.__texto = texto

    @origem.setter
    def origem(self,origem):
        self.__origem = origem