from sqlalchemy import func

import app
from dominios.db import EstudoDicomModel


class EstudoDicomQuery:

    @staticmethod
    def atualiza_registro(studyinstanceuid, estudo_dicom, sessao):
        pass

    @staticmethod
    def busca_clientes(sessao):
        estudos = sessao.query(EstudoDicomModel).all()
        return estudos

    @staticmethod
    def busca_estudo_por_study(sessao, studyinstanceuid):
        estudo = sessao.query(EstudoDicomModel).filter(studyinstanceuid=studyinstanceuid).first()
        return estudo

    @staticmethod
    def set_tuple_of_exames_as_test(sessao: 'SqlAlchemy session',
                                    tuple_of_studies: 'Tuple of studyinstaceuid') -> 'Return a list of sqlAlchemy objects':
        exames = sessao.query(EstudoDicomModel.identificador, EstudoDicomModel.patientname)\
            .filter(EstudoDicomModel.studyinstanceuid.in_(tuple_of_studies)) \
            .filter(EstudoDicomModel.situacao == 'V').filter(EstudoDicomModel.situacao_laudo == 'N').all()
        app.logger.log(f'{exames}')
        sessao.query(EstudoDicomModel).filter(EstudoDicomModel.studyinstanceuid.in_(tuple_of_studies)) \
            .filter(EstudoDicomModel.situacao == 'V').filter(EstudoDicomModel.situacao_laudo == 'N').update(
            {"situacao": "T"}, synchronize_session=False)
        sessao.commit()

    @staticmethod
    def pega_exames_duplicados(sessao):
        return sessao.query(func.count('*'), EstudoDicomModel.accessionnumber).filter(
            EstudoDicomModel.accessionnumber is not None).filter(EstudoDicomModel.accessionnumber != '').group_by(
            EstudoDicomModel.accessionnumber).having(func.count('*') == 2).all()

    @staticmethod
    def lista_exames_por_accession(sessao, accessionnumber):
        result = sessao.query(EstudoDicomModel).filter(accessionnumber == accessionnumber).all()
        return result

    @staticmethod
    def set_as_test(sessao, studyinstanceuid):
        """Sqlalchemy db manager set study as test."""
        app.logger.info('Entrada no metodos de marcar como teste.')
        estudo = sessao.query(EstudoDicomModel).filter_by(studyinstanceuid=studyinstanceuid).first()
        app.logger.info('Exame buscado.')
        if estudo is None:
            raise Exception
        app.logger.info(f'Exame de identificador local nº:{estudo.identificador}, situacao: {estudo.situacao}')
        estudo.situacao = 'T'
        app.logger.info(f"Situação exame {estudo.situacao}")

        sessao.commit()
