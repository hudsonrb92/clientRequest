from configparser import ConfigParser

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class FabricaConexao():

    def conectar(self):
        config = ConfigParser()
        config.read('./config.ini')

        user = config['DATABASE']['user']
        passwd = config['DATABASE']['passwd']
        host = config['DATABASE']['host']
        db = config['DATABASE']['db']
        port = config['DATABASE']['port']

        engine = create_engine(f'postgresql://{user}:{passwd}@{host}:{port}/{db}', pool_pre_ping=True)

        return engine

    def criar_sessao(self):
        conexao = self.conectar()
        Session = sessionmaker()
        Session.configure(bind=conexao)
        session = Session()

        return session