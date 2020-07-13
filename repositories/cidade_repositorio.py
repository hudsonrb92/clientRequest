from queries.cidade_query import CidadeQuery


class CidadeRepositorio:

    @staticmethod
    def lista_cidade_por_cod_ibge(sessao, codigo_ibge):
        return CidadeQuery().lista_cidade_por_cod_ibge(sessao=sessao, codigo_ibge=codigo_ibge)

    @staticmethod
    def lista_cidade_por_identificador(sessao, identificador):
        return CidadeQuery().lista_cidade_por_id(sessao, identificador)
