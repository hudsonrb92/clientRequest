from dominios.db import PessoaEnderecoModel
from queries.pessoa_endereco_query import PessoaEnderecoQuery

class PessoaEnderecoRepositorio():
    def insere_pessoa_endereco(self, sessao, pessoa_endereco):
        novo_pessoa_endereco = PessoaEnderecoModel(identificador_pessoa=pessoa_endereco.identificador_pessoa,
                                                   identificador_endereco=pessoa_endereco.identificador_endereco,
                                                   identificador_tipo_endereco=pessoa_endereco.identificador_tipo_endereco,
                                                   ativa=pessoa_endereco.ativa)
        PessoaEnderecoQuery().insere_pessoa_endereco(sessao=sessao, pessoa_endereco=novo_pessoa_endereco)