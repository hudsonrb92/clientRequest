from dominios.db import PerfilUsuarioEstabelecimentoSaudeModel
from queries.perfil_usuario_estabelecimento_saude_queries import PerfilUsuarioEstabelecimentoSaudeQueries


class PerfilUsuarioEstabelecimentoSaudeRepositorio():
    def insere_pues(self, sessao, perfil_usuario_estabelecumento_saude):
        novo_perfil = PerfilUsuarioEstabelecimentoSaudeModel(identificador_perfil=perfil_usuario_estabelecumento_saude.identificador_perfil,
                                                             identificador_usuario=perfil_usuario_estabelecumento_saude.identificador_usuario,
                                                             identificador_estabelecimento_saude=perfil_usuario_estabelecumento_saude.identificador_estabelecimento_saude,
                                                             data_inicial=perfil_usuario_estabelecumento_saude.data_inicial,
                                                             data_final=perfil_usuario_estabelecumento_saude.data_final)

        PerfilUsuarioEstabelecimentoSaudeQueries().insere_perfil(sessao=sessao,perfil_usuario=novo_perfil)