from dominios.db import CidadeModel

class CidadeQuery():
    def lista_cidade_por_cod_ibge(self, sessao, codigo_ibge):
        cidade = sessao.query(CidadeModel).filter_by(codigo_ibge=codigo_ibge).first()
        return cidade