from dominios.db import PerfilUsuarioEstabelecimentoSaudeModel


class PerfilUsuarioEstabelecimentoSaudeQueries:
    @staticmethod
    def lista_perfil_por_identificador_usuario(sessao, identificador_usuario):
        perfil = sessao.query(PerfilUsuarioEstabelecimentoSaudeModel).filter_by(
            identificador_usuario=identificador_usuario).first()
        return perfil

    @staticmethod
    def insere_perfil(sessao, perfil_usuario):
        sessao.add(perfil_usuario)
