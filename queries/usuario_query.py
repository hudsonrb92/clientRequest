from dominios.db import UsuarioModel


class UsuarioQuery:
    @staticmethod
    def get_usuario_by_identificador_pessoa(sessao, identificador_pessoa):
        usuario = sessao.query(UsuarioModel).filter_by(identificador_pessoa=identificador_pessoa).first()
        return usuario

    @staticmethod
    def insere_usuario(sessao, usuario):
        sessao.add(usuario)

    @staticmethod
    def list_by_login(sessao, login):
        user = sessao.query(UsuarioModel).filter_by(login=login).first()
        return user
