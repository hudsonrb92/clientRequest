from dominios.db import EstadoModel


class EstadoQueries():
    def pega_estado_por_sigla(self,sessao,sigla):
        estado = sessao.query(EstadoModel).filter_by(sigla=sigla).first()
        return estado