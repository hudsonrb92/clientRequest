from dominios.db import EnderecoModel


class EnderecoQuery:
    @staticmethod
    def insereEndereco(sessao, endereco):
        sessao.add(endereco)

    @staticmethod
    def lista_endereco_por_cep(sessao, cep):
        endereco = sessao.query(EnderecoModel).filter_by(cep=cep).first()
        return endereco
