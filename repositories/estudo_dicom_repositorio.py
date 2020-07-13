from dominios.db import logger
from queries.estudo_dicom_queries import EstudoDicomQuery


class EstudoDicomRepositorio:

    @staticmethod
    def listar_estudo(sessao):
        query_estudo = EstudoDicomQuery()
        estudos = query_estudo.busca_clientes(sessao)
        return estudos

    @staticmethod
    def listar_por_studyinstanceuid(sessao, studyinstanceuid):
        query = EstudoDicomQuery().busca_estudo_por_study(sessao=sessao, studyinstanceuid=studyinstanceuid)
        return query

    @staticmethod
    def set_tuple_as_test(sessao, tuple_of_studies):
        EstudoDicomQuery().set_tuple_of_exames_as_test(sessao, tuple_of_studies)

    @staticmethod
    def marcar_exames_como_teste(lista_de_exames: 'Lista de exames', sessao: 'SqlAlchemy session'):
        """lista_de_exames must have in each of item the propertie studyinstanceuid"""
        logger.info("Entrada da função de marcar exames como teste.")
        for exame in lista_de_exames:
            logger.info(f"Exame de studyinstanceuid: {exame['studyinstanceuid']}.")
            try:
                EstudoDicomQuery().set_as_test(sessao, exame['studyinstanceuid'])
            except Exception as e:
                logger.info(f'Exception {e}')
