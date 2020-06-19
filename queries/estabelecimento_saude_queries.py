from dominios.db import EstabelecimentoSaudeModel

class EstabelecimentoSaudeQueries():
    def pega_estabelecimento_por_cnpj(self,sessao,numero_cnpj):
        estabelecimento = sessao.query(EstabelecimentoSaudeModel).filter_by(numero_cnpj=numero_cnpj).first()
        return estabelecimento

    def pega_primeiro_estabelecimento(self, sessao):
        estabelecimento = sessao.query(EstabelecimentoSaudeModel).order_by(EstabelecimentoSaudeModel.identificador).first()
