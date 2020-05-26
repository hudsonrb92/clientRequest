from dominios.db import EstabelecimentoSaudeModel

class EstabelecimentoSaudeQueries():
    def pega_estabelecimento_por_cnpj(self,sessao,cnpj):
        estabelecimento = sessao.query(EstabelecimentoSaudeModel).filter_by(cnpj=cnpj).first()
        return estabelecimento