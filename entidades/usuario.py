class Usuario:
    def __init__(self, login, senha, administrador, ativo):
        self.__login = login
        self.__senha = senha
        self.__administrador = administrador
        self.__ativo = ativo

    @property
    def login(self):
        return self.__login

    @property
    def senha(self):
        return self.__senha

    @property
    def administrador(self):
        return self.__administrador

    @property
    def ativo(self):
        return self.__ativo

    @login.setter
    def login(self, login):
        self.__login = login

    @senha.setter
    def senha(self,senha):
        self.__senha = senha

    @administrador.setter
    def administrador(self, administrador):
        self.__administrador = administrador

    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo