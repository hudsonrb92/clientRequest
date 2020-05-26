from dominios.db import ProfissionalSaudeModel


class ProfissionalSaudeQueries():
    def lista_por_identificador_pessoa(self, sessao, identificador_pessoa):
        profissional_saude = sessao.query(ProfissionalSaudeModel).filter_by(
            identificador_pessoa=identificador_pessoa).first()
        return profissional_saude

    def inserir_profissional_saude(self, profissional_saude, sessao):
        sessao.add(profissional_saude)
