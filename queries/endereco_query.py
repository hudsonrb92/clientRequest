from dominios.db import EnderecoModel


class EnderecoQuery():
    def insereEndereco(self, sessao, endereco):
        sessao.add(endereco)

    def lista_endereco_por_cep(self, sessao, cep):
        endereco = sessao.query(EnderecoModel).filter_by(cep=cep).first()
        return endereco
