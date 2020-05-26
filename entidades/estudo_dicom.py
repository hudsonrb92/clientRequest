class EstudoDicom():
    def __init__(self, studyinstanceuid, studydate, patientname, situacao_laudo,
                 identificador_prioridade_estudo_dicom, numero_exames_ris, situacao, imagens_disponiveis,
                 origem_registro):
        self.__studyinstanceuid = studyinstanceuid
        self.__studydate = studydate
        self.__patientname = patientname
        self.__situacao_laudo = situacao_laudo
        self.__identificador_prioridade_estudo_dicom = identificador_prioridade_estudo_dicom
        self.__numero_exames_ris = numero_exames_ris
        self.__situacao = situacao
        self.__imagens_disponiveis = imagens_disponiveis
        self.__origem_registro = origem_registro

    @property
    def studyinstanceuid(self):
        return self.__studyinstanceuid

    @property
    def studydate(self):
        return self.__studydate

    @property
    def patientname(self):
        return self.__patientname

    @property
    def situacao_laudo(self):
        return self.__situacao_laudo

    @property
    def identificador_prioridade_estudo_dicom(self):
        return self.__identificador_prioridade_estudo_dicom

    @property
    def numero_exames_ris(self):
        return self.__numero_exames_ris

    @property
    def situacao(self):
        return self.__situacao

    @property
    def imagens_disponiveis(self):
        return self.__imagens_disponiveis

    @property
    def origem_registro(self):
        return self.__origem_registro

    @studydate.setter
    def studydate(self, studydate):
        self.__studydate = studydate

    @patientname.setter
    def patientname(self,patientname):
        self.__patientname = patientname

    @situacao_laudo.setter
    def situacao_laudo(self, situacao_laudo):
        self.__situacao_laudo = situacao_laudo

    @identificador_prioridade_estudo_dicom.setter
    def identificador_prioridade_estudo_dicom(self, identificador_prioridade_estudo_dicom):
        self.__identificador_prioridade_estudo_dicom = identificador_prioridade_estudo_dicom

    @numero_exames_ris.setter
    def numero_exames_ris(self,numero_exames_ris):
        self.__numero_exames_ris = numero_exames_ris

    @origem_registro.setter
    def origem_registro(self,origem_registro):
        self.__origem_registro = origem_registro