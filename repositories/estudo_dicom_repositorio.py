from queries.estudo_dicom_queries import EstudoDicomQuery


class EstudoDicomRepositorio:

    @staticmethod
    def listar_estudo(sessao):
        query_estudo = EstudoDicomQuery()
        estudos = query_estudo.buscaClientes(sessao)
        return estudos

    @staticmethod
    def listar_por_studyinstanceuid(sessao, studyinstanceuid):
        query = EstudoDicomQuery().busca_estudo_por_study(sessao=sessao, studyinstanceuid=studyinstanceuid)
        return query

    @staticmethod
    def marcar_exames_como_teste(lista_de_exames: 'Lista de exames', sessao: 'SqlAlchemy session'):
        """lista_de_exames must have in each of item the propertie studyinstanceuid"""
        for exame in lista_de_exames:
            EstudoDicomQuery().set_as_test(exame['studyinstanceuid'], sessao)
