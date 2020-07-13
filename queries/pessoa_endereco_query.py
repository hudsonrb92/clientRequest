class PessoaEnderecoQuery:
    @staticmethod
    def insere_pessoa_endereco(sessao, pessoa_endereco):
        sessao.add(pessoa_endereco)
