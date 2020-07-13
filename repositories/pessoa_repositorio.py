from dominios.db import PessoaModel
from queries.pessoa_query import PessoaQuery


class PessoaRepositorio:

    @staticmethod
    def pega_pessoa_por_nome(nome, sessao):
        pessoa = PessoaQuery().lista_pessoa_por_nome(nome, sessao)
        return pessoa

    @staticmethod
    def cadastra_pessoa(pessoa, sessao):
        nova_pessoa = PessoaModel(nome=pessoa.nome, data_nascimento=pessoa.data_nascimento,
                                  identificador_sexo=pessoa.identificador_sexo,
                                  identificador_raca=pessoa.identificador_raca, ativa=pessoa.ativa)
        PessoaQuery().insere_pessoa(nova_pessoa, sessao)
