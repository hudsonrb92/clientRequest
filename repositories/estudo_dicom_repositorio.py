from queries.estudo_dicom_queries import EstudoDicomQuery


class EstudoDicomRepositorio():

    def listar_estudo(self, sessao):
        query_estudo = EstudoDicomQuery()
        estudos = query_estudo.buscaClientes(sessao)
        return estudos

    def listar_por_studyinstanceuid(self, sessao, studyinstanceuid):
        query = EstudoDicomQuery().buscaEstudoPorStudy(sessao=sessao, studyinstanceuid=studyinstanceuid)
        return query