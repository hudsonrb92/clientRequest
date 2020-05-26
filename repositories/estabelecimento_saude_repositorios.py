from queries.estabelecimento_saude_queries import EstabelecimentoSaudeQueries


class EstabelecimentoSaudeRepositorio():
    def lista_estabelecimento(self,sessao, cnpj):
        estabelecimento = EstabelecimentoSaudeQueries().pega_estabelecimento_por_cnpj(sessao=sessao, cnpj=cnpj)
        return estabelecimento