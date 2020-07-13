from dominios.db import UsuarioModel
from queries.usuario_query import UsuarioQuery


class UsuarioRepositorio:

    @staticmethod
    def inserir_usuario(usuario, sessao):
        novo_usuario = UsuarioModel(login=usuario.login, senha=usuario.senha, administrador=usuario.administrador,
                                    identificador_pessoa=usuario.identificador_pessoa, ativo=usuario.ativo)
        UsuarioQuery().insere_usuario(sessao=sessao, usuario=novo_usuario)

    @staticmethod
    def busca_user_por_id_pessoa(sessao, identificador_pessoa):
        usuario = UsuarioQuery().get_usuario_by_identificador_pessoa(sessao, identificador_pessoa)
        return usuario

    @staticmethod
    def list_by_login(sessao, login):
        user = UsuarioQuery().list_by_login(sessao, login)
        return user
