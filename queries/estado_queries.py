from dominios.db import EstadoModel


class EstadoQueries:
    @staticmethod
    def pega_estado_por_sigla(sessao, sigla):
        estado = sessao.query(EstadoModel).filter_by(sigla=sigla).first()
        return estado
