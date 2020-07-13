from queries.estabelecimento_saude_queries import EstabelecimentoSaudeQueries


class EstabelecimentoSaudeRepositorio:

    @staticmethod
    def lista_estabelecimento(sessao, numero_cnpj):
        estabelecimento = EstabelecimentoSaudeQueries.pega_estabelecimento_por_cnpj(sessao=sessao,
                                                                                    numero_cnpj=numero_cnpj)
        return estabelecimento

    @staticmethod
    def lista_primeiro_estabelecimento(sessao):
        estabelecimento = EstabelecimentoSaudeQueries().pega_primeiro_estabelecimento(sessao=sessao)
        return estabelecimento
