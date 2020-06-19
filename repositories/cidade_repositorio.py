from queries.cidade_query import CidadeQuery

class CidadeRepositorio():
    def lista_cidade_por_cod_ibge(self, sessao, codigo_ibge):
        return CidadeQuery().lista_cidade_por_cod_ibge(sessao=sessao, codigo_ibge=codigo_ibge)

    def lista_cidade_por_identificador(self, sessao, identificador):
        return CidadeQuery().lista_cidade_por_id(sessao, identificador)
