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