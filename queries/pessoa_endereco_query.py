class PessoaEnderecoQuery():
    def insere_pessoa_endereco(self,sessao, pessoa_endereco):
        sessao.add(pessoa_endereco)