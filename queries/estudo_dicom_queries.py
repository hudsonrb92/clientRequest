from sqlalchemy import func

from dominios.db import EstudoDicomModel


class EstudoDicomQuery():

    @staticmethod
    def atualizaRegistro(studyinstanceuid, estudo_dicom, sessao):
        pass

    @staticmethod
    def buscaClientes(sessao):
        estudos = sessao.query(EstudoDicomModel).all()
        return estudos

    @staticmethod
    def busca_estudo_por_study(studyinstanceuid, sessao):
        estudo = sessao.query(EstudoDicomModel).filter_by(studyinstanceuid=studyinstanceuid).first()
        return estudo

    @staticmethod
    def pega_exames_duplicados(sessao):
        return sessao.query(func.count('*'), EstudoDicomModel.accessionnumber).filter(
            EstudoDicomModel.accessionnumber is not None).filter(EstudoDicomModel.accessionnumber != '').group_by(
            EstudoDicomModel.accessionnumber).having(func.count('*') == 2).all()

    @staticmethod
    def lista_exames_por_accession(sessao, accessionnumber):
        result = sessao.query(EstudoDicomModel).filter(accessionnumber == accessionnumber).all()
        return result

    @staticmethod
    def set_as_test(sessao, studyinstanceuid):
        estudo = sessao.query(EstudoDicomModel).filter_by(studyinstanceuid=studyinstanceuid)
        estudo.situacao = 'T'
        sessao.commit()
