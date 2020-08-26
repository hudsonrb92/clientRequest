from dominios.db import PessoaModel


class PessoaQuery:
    @staticmethod
    def lista_pessoa_por_nome(nome: str, sessao: 'sqlalchemy session') -> 'SqlAlchemy PessoalModel Object':
        pessoa = sessao.query(PessoaModel).filter_by(nome=nome).first()
        return pessoa

    @staticmethod
    def insere_pessoa(pessoa, sessao):
        sessao.add(pessoa)
