from dominios.db import EstabelecimentoSaudeModel


class EstabelecimentoSaudeQueries:
    @staticmethod
    def pega_estabelecimento_por_cnpj(sessao, numero_cnpj):
        estabelecimento = sessao.query(EstabelecimentoSaudeModel).filter_by(numero_cnpj=numero_cnpj).first()
        return estabelecimento

    @staticmethod
    def pega_primeiro_estabelecimento(sessao):
        estabelecimento = sessao.query(EstabelecimentoSaudeModel).order_by(
            EstabelecimentoSaudeModel.identificador).first()
        return estabelecimento
