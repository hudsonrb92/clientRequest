import hashlib
from datetime import datetime

import requests

from credentials import CREDENTIALS
from entidades.endereco import Endereco
from entidades.estudo_dicom import EstudoDicom
from entidades.laudo_estudo_dicom import LaudoEstudoDicom
from entidades.perfil_usuario_estabelecimento_saude import PerfilUsuarioEstabelecimentoSaude
from entidades.pessoa import Pessoa
from entidades.pessoa_endereco import PessoaEndereco
from entidades.profissional_saude import ProfissionalSaude
from entidades.usuario import Usuario
from fabricas import fabrica_conexao
from repositories import pessoa_repositorio, laudo_estudo_dicom_repositorio
from repositories.cidade_repositorio import CidadeRepositorio
from repositories.endereco_repositorio import EnderecoRepositorio
from repositories.estabelecimento_saude_repositorios import EstabelecimentoSaudeRepositorio
from repositories.estado_repositorio import EstadoRepositorio
from repositories.estudo_dicom_repositorio import EstudoDicomRepositorio
from repositories.perfil_usuario_estabelecimento_saude_repositorio import PerfilUsuarioEstabelecimentoSaudeRepositorio
from repositories.pessoa_endereco_repositorio import PessoaEnderecoRepositorio
from repositories.profissional_saude_repositorio import ProfissionalSaudeRepositorio
from repositories.usuario_repositorio import UsuarioRepositorio

identificador_estabelecimento_saude = 53
url_laudo = f'http://sistema.elaudos.com/api/laudos/{identificador_estabelecimento_saude}'
url_estudo = 'http://sistema.elaudos.com/api/estudo/%s'
url_profissional = 'http://sistema.elaudos.com/api/profissional/%s'
url_login = 'http://sistema.elaudos.com/api/login'
url_usuario = 'http://sistema.elaudos.com/api/usuario/%s'
numero_cnpj = '4425244000177'
codigo_ibge = 0
cep = 13036225
hoje = datetime.today()

cred = CREDENTIALS

make_login = requests.post(url=url_login, json=cred)
token = make_login.json()['access_token']
print(token)

head = {'Authorization': 'Bearer ' + token}

laudos = requests.get(url=url_laudo, headers=head).json()

for laudo in laudos:
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
    estudo = requests.get(
        url=url_estudo % identificador_estudo_dicom, headers=head).json()
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
    profissional = requests.get(url=url_profissional % identificador_profissional_saude, headers=head).json()
    assinatura_digitalizada = profissional['assinatura_digitalizada']
    ativo = True
    estado_conselho_trabalho = profissional['estado_conselho_trabalho']['sigla']
    registro_conselho_trabalho = profissional['registro_conselho_trabalho']
    identificador_pessoa = profissional['pessoa']['identificador']
    nome = profissional['pessoa']['nome']
    ativa = True
    pessa_data_nascimento = profissional['pessoa']['data_nascimento']
    identificador_sexo = profissional['pessoa']['identificador_sexo']
    usuario_req = requests.get(url=url_usuario % identificador_pessoa, headers=head).json()
    login = usuario_req['login']
    login = str(login + registro_conselho_trabalho.split(' ')[0])
    senha = registro_conselho_trabalho.split(' ')[0]
    senha_hasheada = hashlib.md5(senha.encode('utf8')).hexdigest()
    administrador = usuario_req['administrador']
    usuario_ativo = True

    fabrica = fabrica_conexao.FabricaConexao()
    sessao = fabrica.criar_sessao()

    pessoaEntidade = Pessoa(nome=nome, ativa=ativa)
    pessoaEntidade.identificador_sexo = identificador_sexo
    pessoaEntidade.data_nascimento = pessa_data_nascimento
    pessoaEntidade.identificador_raca = 1

    usuarioEntidade = Usuario(login=login, senha=senha_hasheada, administrador='administrador', ativo=usuario_ativo)
    laudoEntidade = LaudoEstudoDicom(data_hora_emissao=data_hora_emissao,
                                     identificador_estudo_dicom=identificador_estudo_dicom,
                                     integrado=integrado, situacao=situacao, situacao_envio_his=situacao_envio_his,
                                     texto=texto,
                                     identificador_profissional_saude=identificador_profissional_saude)
    laudoEntidade.numero_exames_relacionados = numero_exames_relacionados
    laudoEntidade.identificador_laudo_elaudos = identificador_laudo_elaudos

    estado_local = EstadoRepositorio().pega_estado_por_sigla(sessao=sessao, sigla=estado_conselho_trabalho)

    identificador_estabelecimento_saude_local = EstabelecimentoSaudeRepositorio().lista_estabelecimento(sessao=sessao,
                                                                                                        numero_cnpj=numero_cnpj)

    # Criar Endereco Entidade
    endereco_entidade = Endereco(identificador_tipo_endereco='Avenida', logradouro='Gerado Por Integração', ativo=True)
    endereco_entidade.complemento = ''
    endereco_entidade.bairro = 'Centro'
    endereco_entidade.cep = cep

    # Criar entidade Profissional de saude
    profissional_saudeEntidade = ProfissionalSaude(ativo=ativo, identificador_pessoa=identificador_pessoa,
                                                   registro_conselho_trabalho=registro_conselho_trabalho,
                                                   identificador_estado_conselho_trabalho=estado_local.identificador,
                                                   identificador_tipo_conselho_trabalho=1)
    profissional_saudeEntidade.assinatura_digitalizada = assinatura_digitalizada

    pessoa_local = pessoa_repositorio.PessoaRepositorio().pega_pessoa_por_nome(pessoaEntidade.nome, sessao)

    if pessoa_local:
        estudo_local = EstudoDicomRepositorio().listar_por_studyinstanceuid(sessao,
                                                                                          studyinstanceuid)
        if estudo_local:
            identificador_estudo_local = estudo_local.identificador
        else:
            print("Exame Nao Existente")
            continue

        laudoEntidade.identificador_profissional_saude = profissional_saude_local.identificador
        laudoEntidade.identificador_estudo_dicom = identificador_estudo_local
        laudoEntidade.integrado = True

        if estudo_local.situacao_laudo != 'S':
            profissional_saude_local = ProfissionalSaudeRepositorio().listar_profissional_saude(sessao,
                                                                                                pessoa_local.identificador)
            laudo_estudo_dicom_repositorio.LaudoEstudoDicomRepositorio().insere_laudo(laudo=laudoEntidade, sessao=sessao)
            url_to_put = f'http://sistema.elaudos.com/api/{laudoEntidade.identificador_laudo_elaudos}'
            integra = requests.put(url=url_to_put, headers=head)
        else:
            print("Laudo Ja publicado")
            integra = requests.put(url=url_to_put, headers=head)

    else:
        # Criar pessoa
        pessoa_repositorio.PessoaRepositorio().cadastra_pessoa(pessoa=pessoaEntidade, sessao=sessao)
        pessoa_local_nova = pessoa_repositorio.PessoaRepositorio().pega_pessoa_por_nome(nome=pessoaEntidade.nome, sessao=sessao)

        # Criar Endereco
        cidade = CidadeRepositorio().lista_cidade_por_cod_ibge(sessao=sessao, codigo_ibge=codigo_ibge)
        endereco_entidade.identificador_cidade = cidade.identificador
        EnderecoRepositorio().insere_endereco(sessao=sessao, endereco=endereco_entidade)

        # Criar Profissional de saude
        profissional_saudeEntidade.identificador_pessoa = pessoa_local_nova.identificador
        ProfissionalSaudeRepositorio().inserir_profissional_saude(sessao=sessao,
                                                                  profissional_saude=profissional_saudeEntidade)

        # Criar Pessoa_endereco
        identificador_endereco_novo = EnderecoRepositorio.lista_endereco_por_cep(sessao=sessao, cep=cep)
        pessoa_endereco_entidade = PessoaEndereco(identificador_pessoa=pessoa_local_nova.identificador,
                                                  identificador_endereco=identificador_endereco_novo,
                                                  identificador_tipo_uso_endereco='Comercial', ativa=True)
        PessoaEnderecoRepositorio().insere_pessoa_endereco(sessao=sessao, pessoa_endereco=pessoa_endereco_entidade)

        # Criar Usuário
        usuarioEntidade.identificador_pessoa = pessoa_local_nova.identificador
        UsuarioRepositorio().inserir_usuario(usuario=usuarioEntidade, sessao=sessao)

        # Perfil Usuário Estabelecimento Saude
        perfil_usuario_estabelecimento_saude_entidade = PerfilUsuarioEstabelecimentoSaude(
            identificador_perfil='ROLE_MEDICO_EXECUTOR',
            identificador_estabelecimento_saude=identificador_estabelecimento_saude_local,
            data_inicial=f'{hoje.year}-{hoje.month:02}-{hoje.day:02}')

        identificador_usuario_novo = UsuarioRepositorio().busca_user_por_id_pessoa(sessao=sessao,
                                                                                   identificador_pessoa=pessoa_local_nova.identificador).identificador

        perfil_usuario_estabelecimento_saude_entidade.identificador_usuario = identificador_usuario_novo
        perfil_usuario_estabelecimento_saude_entidade.data_final = data_inicial = f'{hoje.year}-{hoje.month:02}-{hoje.day:02}'
        PerfilUsuarioEstabelecimentoSaudeRepositorio().insere_pues(sessao=sessao,
                                                                   perfil_usuario_estabelecumento_saude=perfil_usuario_estabelecimento_saude_entidade)
