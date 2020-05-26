class AnexoEstudoDicom():
    def __init__(self, identificador_estudo_dicom, nome_arquivo, conteudo_arquivo):
        self.__identificador_estudo_dicom = identificador_estudo_dicom
        self.__nome_arquivo = nome_arquivo
        self.__conteudo_arquivo = conteudo_arquivo

    @property
    def identificador_estudo_dicom(self):
        return self.__identificador_estudo_dicom

    @property
    def nome_arquivo(self):
        return self.__nome_arquivo

    @property
    def conteudo_arquivo(self):
        return self.__conteudo_arquivo

    @identificador_estudo_dicom.setter
    def identificador_estudo_dicom(self,identificador_estudo_dicom):
        self__identificador_estudo_dicom = identificador_estudo_dicom

    @nome_arquivo.setter
    def nome_arquivo(self,nome_arquivo):
        self.__nome_arquivo = nome_arquivo

    @conteudo_arquivo.setter
    def conteudo_arquivo(self, conteudo_arquivo):
        self.__conteudo_arquivo = conteudo_arquivo