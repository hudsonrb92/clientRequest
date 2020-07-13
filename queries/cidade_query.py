from dominios.db import CidadeModel


class CidadeQuery:
    @staticmethod
    def lista_cidade_por_cod_ibge(sessao, codigo_ibge):
        cidade = sessao.query(CidadeModel).filter_by(
            codigo_ibge=codigo_ibge).first()
        return cidade

    @staticmethod
    def lista_cidade_por_id(sessao, identificador):
        cidade = sessao.query(CidadeModel).filter_by(
            identificador=identificador).first()
        return cidade
