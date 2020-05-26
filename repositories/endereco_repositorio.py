from dominios.db import EnderecoModel
from queries.endereco_query import EnderecoQuery

class EnderecoRepositorio():
    def insere_endereco(self, sessao, endereco):
        endereco_novo = EnderecoModel(identificador_tipo_endereco=endereco.identificador_tipo_endereco,
                                      logradouro=endereco.logradouro,
                                      complemento=endereco.complemento, bairro=endereco.bairro, cep=endereco.cep,
                                      identificador_cidade=endereco.identificador_cidade,
                                      ativo=endereco.ativo)
        EnderecoQuery().insereEndereco(sessao=sessao,endereco=endereco_novo)

    def lista_endereco_por_cep(self,sessao,cep):
        return EnderecoQuery().lista_endereco_por_cep(sessao=sessao,cep=cep)