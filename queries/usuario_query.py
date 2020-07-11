from dominios.db import UsuarioModel

class UsuarioQuery():
    def get_usuario_by_identificador_pessoa(self,sessao, identificador_pessoa):
        usuario = sessao.query(UsuarioModel).filter_by(identificador_pessoa = identificador_pessoa).first()
        return usuario

    def insere_usuario(self, sessao, usuario):
        sessao.add(usuario)

    def list_by_login(self, sessao, login):
        user = sessao.query(UsuarioModel).filter_by(login=login).first()
        return user