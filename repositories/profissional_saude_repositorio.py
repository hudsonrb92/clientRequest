from base64 import b64decode

from dominios.db import ProfissionalSaudeModel
from queries.profissional_saude_queries import ProfissionalSaudeQueries


class ProfissionalSaudeRepositorio:

    @staticmethod
    def inserir_profissional_saude(sessao, profissional_saude):
        assinatura_decodada = b64decode(profissional_saude.assinatura_digitalizada)
        novo_profissional_saude = ProfissionalSaudeModel(identificador_pessoa=profissional_saude.identificador_pessoa,
                                                         identificador_tipo_conselho_trabalho=1,
                                                         identificador_estado_conselho_trabalho=profissional_saude
                                                         .identificador_estado_conselho_trabalho,
                                                         registro_conselho_trabalho=profissional_saude
                                                         .registro_conselho_trabalho,
                                                         ativo=profissional_saude.ativo,
                                                         assinatura_digitalizada=assinatura_decodada)
        ProfissionalSaudeQueries().inserir_profissional_saude(profissional_saude=novo_profissional_saude, sessao=sessao)

    @staticmethod
    def listar_profissional_saude(sessao, identificador_pessoa):
        profissional = ProfissionalSaudeQueries(). \
            lista_por_identificador_pessoa(sessao=sessao, identificador_pessoa=identificador_pessoa)
        return profissional

    @staticmethod
    def lista_profissional_por_registro(sessao, registro):
        profissional = ProfissionalSaudeQueries().lista_por_registro(sessao, registro)
        return profissional
