from dominios.db import LaudoEstudoDicomModel
from queries.laudos_estudo_dicom_queries import LaudoEstudoDicomQuery


class LaudoEstudoDicomRepositorio:
    def insere_laudo(self, laudo, sessao):
        laudoModel = LaudoEstudoDicomModel(data_hora_emissao=laudo.data_hora_emissao,
                                           identificador_estudo_dicom=laudo.identificador_estudo_dicom,
                                           integrado=laudo.integrado,
                                           numero_exames_relacionados=laudo.numero_exames_relacionados,
                                           situacao=laudo.situacao, situacao_envio_his=laudo.situacao_envio_his,
                                           texto=laudo.texto,
                                           identificador_profissional_saude=laudo.identificador_profissional_saude)
        LaudoEstudoDicomQuery().insere_laudo(sessao=sessao, laudo=laudoModel)
