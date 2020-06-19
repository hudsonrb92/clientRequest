from sqlalchemy import func

from dominios.db import EstudoDicomModel


class EstudoDicomQuery():

    def atualizaRegistro(self, studyinstanceuid, estudo_dicom, sessao):
        pass

    def buscaClientes(self, sessao):
        estudos = sessao.query(EstudoDicomModel).all()
        return estudos

    def buscaEstudoPorStudy(self, studyinstanceuid, sessao):
        estudo = sessao.query(EstudoDicomModel).filter_by(studyinstanceuid=studyinstanceuid).first()
        return estudo

    def pega_exames_duplicados(self, sessao):
        return sessao.query(func.count('*'), EstudoDicomModel.accessionnumber).filter(
            EstudoDicomModel.accessionnumber is not None).filter(EstudoDicomModel.accessionnumber != '').group_by(
            EstudoDicomModel.accessionnumber).having(func.count('*') == 2).all()

    def lista_exames_por_accession(self, sessao, accessionnumber):
        result = sessao.query(EstudoDicomModel).filter(accessionnumber == accessionnumber).all()
        return result