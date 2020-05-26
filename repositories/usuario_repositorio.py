from dominios.db import UsuarioModel
from queries.usuario_query import UsuarioQuery


class UsuarioRepositorio():
    def inserir_usuario(self, usuario, sessao):
        novo_usuario = UsuarioModel(login=usuario.login, senha=usuario.senha, administrador=usuario.administrador,
                                    identificador_pessoa=usuario.identificador_pessoa, ativo=usuario.ativo)
        UsuarioQuery().insere_usuario(sessao=sessao, usuario=novo_usuario)

    def busca_user_por_id_pessoa(self, sessao, identificador_pessoa):
        usuario = UsuarioQuery().get_usuario_by_identificador_pessoa(sessao, identificador_pessoa)
        return usuario
