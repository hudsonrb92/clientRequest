import hashlib
from datetime import datetime

import requests

from credentials import CREDENTIALS
from entidades.endereco import Endereco
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

def now():
    hoje = datetime.now()
    hoje_data_hora = f"{hoje.day:02}/{hoje.month:02}/{hoje.year} {hoje.hour:02}:{hoje.minute:02}:{hoje.second:02}"
    return (hoje_data_hora)

fabrica = fabrica_conexao.FabricaConexao()
sessao = fabrica.criar_sessao()
print(f"{now()} -> Sessão criada ...")

identificador_estabelecimento_saude = 47
estabelecimento_local = EstabelecimentoSaudeRepositorio().lista_primeiro_estabelecimento(sessao)
numero_cnpj = estabelecimento_local.numero_cnpj
print(f"{now()} --> Número de CNPJ: {numero_cnpj}")

cidade_local = CidadeRepositorio().lista_cidade_por_identificador(sessao,estabelecimento_local.endereco.identificador_cidade)
codigo_ibge = cidade_local.codigo_ibge
print(f"{now()} -> Codigo IBGE: {codigo_ibge}")

cep = estabelecimento_local.endereco.cep
print(f"{now()} -> Cep: {cep}")

url_laudo = f'http://sistema.elaudos.com/api/laudos/{identificador_estabelecimento_saude}'
url_estudo = 'http://sistema.elaudos.com/api/estudo/%s'
url_profissional = 'http://sistema.elaudos.com/api/profissional/%s'
url_login = 'http://sistema.elaudos.com/api/login'
url_usuario = 'http://sistema.elaudos.com/api/usuario/%s'

cred = CREDENTIALS

make_login = requests.post(url=url_login, json=cred)
token = make_login.json()['access_token']

head = {'Authorization': 'Bearer ' + token}

laudos = requests.get(url=url_laudo, headers=head).json()
print(f"{now()} -> Quantidade de laudos para integrar = {len(laudos)}")

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


    pessoaEntidade = Pessoa(nome=nome, ativa=ativa)
    pessoaEntidade.identificador_sexo = identificador_sexo
    pessoaEntidade.data_nascimento = pessa_data_nascimento
    pessoaEntidade.identificador_raca = 1

    print(f"{now()} -> Pessoa entidade Criada")

    usuarioEntidade = Usuario(login=login, senha=senha_hasheada, administrador=False, ativo=usuario_ativo)


    print(f"{now()} -> Usuario entidade Criado")
    laudoEntidade = LaudoEstudoDicom(data_hora_emissao=data_hora_emissao,
                                     identificador_estudo_dicom=identificador_estudo_dicom,
                                     situacao=situacao, situacao_envio_his=situacao_envio_his,
                                     texto=texto,
                                     identificador_profissional_saude=identificador_profissional_saude)
    laudoEntidade.numero_exames_relacionados = numero_exames_relacionados
    laudoEntidade.identificador_laudo_elaudos = identificador_laudo_elaudos


    print(f"{now()} -> Laudo Entidade Criado")

    estado_local = EstadoRepositorio().pega_estado_por_sigla(sessao=sessao, sigla=estado_conselho_trabalho)

    identificador_estabelecimento_saude_local = EstabelecimentoSaudeRepositorio().lista_estabelecimento(sessao=sessao,
                                                                                                        numero_cnpj=numero_cnpj)
    identificador_estabelecimento_saude_local = identificador_estabelecimento_saude_local.identificador

    # Criar Endereco Entidade
    endereco_entidade = Endereco(identificador_tipo_endereco='Avenida', logradouro='Gerado Por Integração', ativo=True)
    endereco_entidade.complemento = ''
    endereco_entidade.bairro = 'Centro'
    endereco_entidade.cep = cep

    print(f"{now()} -> Endereco Criado")

    # Criar entidade Profissional de saude
    profissional_saudeEntidade = ProfissionalSaude(ativo=ativo, identificador_pessoa=identificador_pessoa,
                                                   registro_conselho_trabalho=registro_conselho_trabalho,
                                                   identificador_estado_conselho_trabalho=estado_local.identificador,
                                                   identificador_tipo_conselho_trabalho=1)
    profissional_saudeEntidade.assinatura_digitalizada = assinatura_digitalizada

    print(f"{now()} -> profissional_saudeEntidade Criado")
    pessoa_local = pessoa_repositorio.PessoaRepositorio().pega_pessoa_por_nome(pessoaEntidade.nome, sessao)

    if pessoa_local:

        print(f"{now()} -> Usuario ja existente")
        estudo_local = EstudoDicomRepositorio().listar_por_studyinstanceuid(sessao,
                                                                            studyinstanceuid)
        if estudo_local:
            identificador_estudo_local = estudo_local.identificador
            print(f"{now()} -> Exame Encontrado")
        else:
            print(f"{now()} -> Exame Nao Existente")
            continue

        profissional_saude_local = ProfissionalSaudeRepositorio().listar_profissional_saude(sessao,
                                                                                            pessoa_local.identificador)
        laudoEntidade.identificador_profissional_saude = profissional_saude_local.identificador
        laudoEntidade.identificador_estudo_dicom = identificador_estudo_local

        if estudo_local.situacao_laudo == 'N' and situacao=='D':
            print(f"{now()} -> Publicando Exame.")
            laudo_estudo_dicom_repositorio.LaudoEstudoDicomRepositorio().insere_laudo(laudo=laudoEntidade,
                                                                                      sessao=sessao)
            url_to_put = f'http://sistema.elaudos.com/api/laudo/{laudoEntidade.identificador_laudo_elaudos}'
            integra = requests.put(url=url_to_put, headers=head)
        else:
            print(f"{now()} -> Laudo Ja publicado")
            url_to_put = f'http://sistema.elaudos.com/api/laudo/{laudoEntidade.identificador_laudo_elaudos}'
            integra = requests.put(url=url_to_put, headers=head)
            print(f'{now()} {integra}')

    else:
        print(f"{now()} -> Iniciando Processo de criação de usuario")
        # Criar pessoa
        try:
            pessoa_repositorio.PessoaRepositorio().cadastra_pessoa(pessoa=pessoaEntidade, sessao=sessao)
            sessao.commit()
            pessoa_local_nova = pessoa_repositorio.PessoaRepositorio().pega_pessoa_por_nome(nome=pessoaEntidade.nome,
                                                                                            sessao=sessao)

        except Exception as e:
            print(f'{now()} .............................................................\n{e}\
                \n.............................................................')


        print(f"{now()} -> Iniciando Processo de criação de Endereco")
        # Criar Endereco
        cidade = CidadeRepositorio().lista_cidade_por_cod_ibge(sessao=sessao, codigo_ibge=codigo_ibge)
        endereco_entidade.identificador_cidade = cidade.identificador
        endereco_repo = EnderecoRepositorio()
        endereco_repo.insere_endereco(sessao=sessao, endereco=endereco_entidade)


        print(f"{now()} -> Iniciando Processo de criação de Profissional de saude")
        # Criar Profissional de saude
        profissional_saudeEntidade.identificador_pessoa = pessoa_local_nova.identificador
        profi_repo = ProfissionalSaudeRepositorio()
        profi_repo.inserir_profissional_saude(sessao=sessao,
                                              profissional_saude=profissional_saudeEntidade)


        print(f"{now()} -> Iniciando Processo de criação de Pessoa_endereco")
        # Criar Pessoa_endereco
        identificador_endereco_novo = EnderecoRepositorio().lista_endereco_por_cep(sessao=sessao, cep=cep).identificador
        pessoa_endereco_entidade = PessoaEndereco(identificador_pessoa=pessoa_local_nova.identificador,
                                                  identificador_endereco=identificador_endereco_novo,
                                                  identificador_tipo_uso_endereco='Comercial', ativa=True)
        pessoa_ende_repo = PessoaEnderecoRepositorio()
        pessoa_ende_repo.insere_pessoa_endereco(sessao=sessao, pessoa_endereco=pessoa_endereco_entidade)


        print(f"{now()} -> Iniciando Processo de criação de Usuário")
        # Criar Usuário
        usuarioEntidade.identificador_pessoa = pessoa_local_nova.identificador
        usuario_repo = UsuarioRepositorio()
        usuario_repo.inserir_usuario(usuario=usuarioEntidade, sessao=sessao)


        print(f"{now()} -> Iniciando Processo de criação de Perfil Usuário Estabelecimento Saude")
        # Perfil Usuário Estabelecimento Saude
        perfil_usuario_estabelecimento_saude_entidade = PerfilUsuarioEstabelecimentoSaude(
            identificador_perfil='ROLE_MEDICO_EXECUTOR',
            identificador_estabelecimento_saude=identificador_estabelecimento_saude_local,
            data_inicial=f'{hoje.year}-{hoje.month:02}-{hoje.day:02}')

        identificador_usuario_novo = UsuarioRepositorio().busca_user_por_id_pessoa(sessao=sessao,
                                                                                   identificador_pessoa=pessoa_local_nova.identificador)

        perfil_usuario_estabelecimento_saude_entidade.identificador_usuario = identificador_usuario_novo.identificador
        perfil_usuario_estabelecimento_saude_entidade.data_final = data_inicial = f'{hoje.year}-{hoje.month:02}-{hoje.day:02}'
        pues_repo = PerfilUsuarioEstabelecimentoSaudeRepositorio()
        pues_repo.insere_pues(sessao=sessao,
                              perfil_usuario_estabelecumento_saude=perfil_usuario_estabelecimento_saude_entidade)

    sessao.commit()
