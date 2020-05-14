from configparser import ConfigParser

from sqlalchemy import create_engine


class FabricaConexao():

    def conectar(self):
        config = ConfigParser()
        config.read('./config.ini')

        user = config['DATABASE']['']
        passwd = config['DATABASE']['passwd']
        host = config['DATABASE']['host']
        db = config['DATABASE']['db']
        port = config['DATABASE']['port']

        engine = create_engine(f'postgresql://{user}:{passwd}@{host}:{port}/{db}')

        return engine
