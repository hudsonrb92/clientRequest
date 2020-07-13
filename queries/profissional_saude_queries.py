from dominios.db import ProfissionalSaudeModel


class ProfissionalSaudeQueries:
    @staticmethod
    def lista_por_identificador_pessoa(sessao, identificador_pessoa):
        profissional_saude = sessao.query(ProfissionalSaudeModel).filter_by(
            identificador_pessoa=identificador_pessoa).first()
        return profissional_saude

    @staticmethod
    def inserir_profissional_saude(profissional_saude, sessao):
        sessao.add(profissional_saude)

    @staticmethod
    def lista_por_registro(sessao, registo):
        profissional = sessao.query(ProfissionalSaudeModel).filter_by(registro_conselho_trabalho=registo).first()
        return profissional
