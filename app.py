import hashlib

import medicos as medicos
import requests

from credentials import CREDENTIALS
from dominios.db import logger
from entidades.laudo_estudo_dicom import LaudoEstudoDicom
from fabricas.fabrica_conexao import FabricaConexao
from repositories.estabelecimento_saude_repositorios import EstabelecimentoSaudeRepositorio
from repositories.estado_repositorio import EstadoRepositorio
from repositories.estudo_dicom_repositorio import EstudoDicomRepositorio as edr
from repositories.laudo_estudo_dicom_repositorio import LaudoEstudoDicomRepositorio as ledr
from repositories.pessoa_repositorio import PessoaRepositorio as pr
from repositories.profissional_saude_repositorio import ProfissionalSaudeRepositorio as psr
from repositories.usuario_repositorio import UsuarioRepositorio

def integra():

    sessao = FabricaConexao().criar_sessao()
    logger.info('Sessão criada ...')
    identificador_estabelecimento_saude = 53
    estabelecimento_local = EstabelecimentoSaudeRepositorio.lista_primeiro_estabelecimento(
        sessao)
    logger.info(' %s', estabelecimento_local.nome_fantasia)

    url_laudo = f'http://sistema.elaudos.com/api/laudos/{identificador_estabelecimento_saude}'
    url_estudo = 'http://sistema.elaudos.com/api/estudo/%s'
    url_profissional = 'http://sistema.elaudos.com/api/profissional/%s'
    url_login = 'http://sistema.elaudos.com/api/login'
    url_usuario = 'http://sistema.elaudos.com/api/usuario/%s'
    url_exames_sem_laudo = f'http://sistema.elaudos.com/api/estudoSemLaudo/{identificador_estabelecimento_saude}'
    cred = CREDENTIALS
    make_login = requests.post(url=url_login, json=cred)
    token = make_login.json()['access_token']
    head = {'Authorization': 'Bearer ' + token}
    logger.info("Lista de laudos recuperada.")
    # Exames sem laudo na elaudos
    exames_sem_laudo = requests.get(url=url_exames_sem_laudo, headers=head).json()
    logger.info(
        f"O numero de exames sem laudos na elaudos é de {len(exames_sem_laudo)}.")

    # Pegar exames localmente que não estejam marcados como teste.
    # if exames_sem_laudo is list:
    #     studies = [exame['studyinstanceuid'] for exame in exames_sem_laudo]
    #     studies = tuple(studies)
    #     logger.info(f'{studies}')
    #     # Marca exames localmente como que estejam sem laudo e que tenham situação valida como teste.
    #     exams_to_set_as_test = edr.set_tuple_as_test(sessao, studies)
    #     logger.info("Exames marcados como teste.")

    laudos = requests.get(url=url_laudo, headers=head).json()
    logger.info(f"Quantidade de laudos para integrar = {len(laudos)}")
    for laudo in laudos:
        # Pega atributos de Estudo_Dicom
        data_hora_emissao = laudo['data_hora_emissao']
        data_hora_revisao = laudo['data_hora_revisao']
        identificador_laudo_elaudos = laudo['identificador']
        identificador_estudo_dicom = laudo['identificador_estudo_dicom']
        integrado = laudo['integrado']
        numero_exames_relacionados = laudo['numero_exames_relacionados']
        situacao = laudo['situacao']
        situacao_envio_his = laudo['situacao_envio_his']
        texto = laudo['texto']
        identificador_profissional_saude = laudo['identificador_profissional_saude']
        estudo = requests.get(url=url_estudo %
                                  identificador_estudo_dicom, headers=head).json()
        accessionnumber = estudo['accessionnumber']
        chave_primaria_origem = estudo['chave_primaria_origem']
        data_hora_inclusao = estudo['data_hora_inclusao']
        data_hora_ultima_alteracao = estudo['data_hora_ultima_alteracao']
        data_hora_validacao = estudo['data_hora_validacao']
        modalitiesinstudy = estudo['modalitiesinstudy']
        nome_mae = estudo['nome_mae']
        numberofinstances = estudo['numberofinstances']
        numero_exames_ris = estudo['numero_exames_ris']
        patientbirthdate = estudo['patientbirthdate']
        patientid = estudo['patientid']
        patientname = estudo['patientname']
        patientsex = estudo['patientsex']
        situacao_estudo = estudo['situacao']
        situacao_laudo_estudo = estudo['situacao_laudo']
        studydescription = estudo['studydescription']
        studyid = estudo['studyid']
        studyinstanceuid = estudo['studyinstanceuid']
        studytime = estudo['studytime']
        profissional = requests.get(
            url=url_profissional % identificador_profissional_saude, headers=head).json()
        assinatura_digitalizada = profissional['assinatura_digitalizada']
        ativo = True
        estado_conselho_trabalho = profissional['estado_conselho_trabalho']['sigla']
        registro_conselho_trabalho = profissional['registro_conselho_trabalho']
        identificador_pessoa = profissional['pessoa']['identificador']
        nome = profissional['pessoa']['nome']
        ativa = True
        pessa_data_nascimento = profissional['pessoa']['data_nascimento']
        identificador_sexo = profissional['pessoa']['identificador_sexo']
        usuario_req = requests.get(url=url_usuario %
                                       identificador_pessoa, headers=head).json()
        login = usuario_req['login']
        login = str(login + registro_conselho_trabalho.split(' ')[0])
        senha = registro_conselho_trabalho.split(' ')[0]
        senha_hasheada = hashlib.md5(senha.encode('utf8')).hexdigest()
        usuario_ativo = True

        # Primeiro devemos buscar o exame localmente
        estudo_local = edr().listar_por_studyinstanceuid(sessao, studyinstanceuid)
        # Caso o estudo exista fazemos as verificações
        if estudo_local:
            # Verifica se existe pessoa, profissional_saude, usuario localmente
            pessoa_local = pr().pega_pessoa_por_nome(nome, sessao)
            # Busca profissional_saude localmente
            ps_local = psr().lista_profissional_por_registro(
                sessao, registro_conselho_trabalho)
            # Busca usuario_local
            usuario_local = UsuarioRepositorio().list_by_login(sessao, login)

            # Criamos aqui a entidade do laudo para não ter que criar novamente no else
            laudo_entidade = LaudoEstudoDicom(data_hora_emissao=data_hora_emissao,
                                              identificador_estudo_dicom=identificador_estudo_dicom,
                                              situacao=situacao, situacao_envio_his=situacao_envio_his,
                                              texto=texto,
                                              identificador_profissional_saude=identificador_profissional_saude)

            laudo_entidade.numero_exames_relacionados = numero_exames_relacionados
            laudo_entidade.identificador_laudo_elaudos = identificador_laudo_elaudos
            logger.info(
                f"Laudo Entidade Criado emitido as:{laudo_entidade.data_hora_emissao}")
            estado_local = EstadoRepositorio().pega_estado_por_sigla(
                sessao=sessao, sigla=estado_conselho_trabalho)
            logger.info(
                f"Estado banco de dados local - {estado_local.nome}-{estado_local.sigla}")
            identificador_estabelecimento_saude_local = estabelecimento_local.identificador

            # Caso nenhum dos 3 existam criar o médico novo
            if not (pessoa_local or ps_local or usuario_local):
                try:
                    ps_novo = medicos.Medicos \
                        .cadastra_medico(sessao=sessao, crm=registro_conselho_trabalho,
                                         uf=estado_conselho_trabalho, nome=nome,
                                         perfil='ROLE_MEDICO_EXECUTOR',
                                         assinatura=assinatura_digitalizada, login=login,
                                         identificador_estabelecimento_saude=identificador_estabelecimento_saude_local)
                    logger.info(f'Profissional de saude cadastrado.')
                    laudo_entidade.identificador_profissional_saude = ps_novo.identificador
                    logger.info(
                        f'Identificador Profissional = {ps_novo.identificador}')
                except Exception as e:
                    logger.info(f'Erro ao cadastrar médico {e}')
                    raise Exception('Um erro ao cadastrar paciente')
                if estudo_local.situacao_laudo == 'N' and situacao == 'D':
                    try:
                        ledr().insere_laudo(laudo=laudo_entidade, sessao=sessao)
                        estudo_local.situacao = 'V'
                        sessao.commit()
                        logger.info(f'Laudo inserido. Study -> {studyinstanceuid}')
                        logger.info(f'Paciente -> {patientname} - {patientid}')
                        url_to_put = f'http://sistema.elaudos.com/api/laudo/{laudo_entidade.identificador_laudo_elaudos}'
                        integra = requests.put(url=url_to_put, headers=head)
                    except Exception as e:
                        sessao.rollback()
                        logger.info(f'Ocorreu um erro ao inserir o laudo {e}')
                        raise Exception
                elif (estudo_local.situacao_laudo == 'S' or
                      estudo_local.situacao_laudo == 'C' or
                      estudo_local.situacao_laudo == 'G') and situacao == 'D':
                    logger.info(
                        f'Laudo já emitido localmente, mudando sitauação do laudo na elaudos.')
                    url_to_put = f'http://sistema.elaudos.com/api/laudo/{laudo_entidade.identificador_laudo_elaudos}'
                    integra = requests.put(url=url_to_put, headers=head)

            else:
                logger.info(
                    f'Profissional de Saúde encontrado sem necessidade de nova criação')
                # Cria Laudo entidade

                laudo_entidade.identificador_estudo_dicom = estudo_local.identificador
                if pessoa_local:
                    laudo_entidade.identificador_profissional_saude = pessoa_local.profissional_saude[
                        0].identificador
                elif ps_local:
                    laudo_entidade.identificador_profissional_saude = ps_local.identificador
                elif usuario_local:
                    laudo_entidade.identificador_profissional_saude = usuario_local.pessoa.profissional_saude[
                        0].identificador
                else:
                    logger.info(f'Inconcistência no profissional de saude')
                    # Caso estudo local ainda esteja sem laudo e situação do laudo na
                    # Elaudos esteja como definitivo podemos publicar o laudo
                if estudo_local.situacao_laudo == 'N' and situacao == 'D':
                    try:
                        ledr().insere_laudo(laudo=laudo_entidade, sessao=sessao)
                        estudo_local.situacao = 'V'
                        sessao.commit()
                        logger.info(f'Laudo id: {laudo_entidade.identificador_laudo_elaudos}, inserido no estudo_local:\
    {estudo_local.identificador}')
                        url_to_put = f'http://sistema.elaudos.com/api/laudo/{laudo_entidade.identificador_laudo_elaudos}'
                        integra = requests.put(url=url_to_put, headers=head)
                    except Exception as e:
                        logger.info(f"Erro ao inserir laudo no exame : {e}")
                elif (estudo_local.situacao_laudo == 'S' or
                      estudo_local.situacao_laudo == 'C' or
                      estudo_local.situacao_laudo == 'G') and situacao == 'D':
                    logger.info(
                        f'Laudo já emitido localmente, mudando sitauação do laudo na elaudos.')
                    url_to_put = f'http://sistema.elaudos.com/api/laudo/{laudo_entidade.identificador_laudo_elaudos}'
                    integra = requests.put(url=url_to_put, headers=head)
        else:
            logger.info('Estudo não encontrado localmente.')
            logger.info(
                f'{studyinstanceuid} - {identificador_laudo_elaudos} - {identificador_estudo_dicom}')

    sessao.close()
