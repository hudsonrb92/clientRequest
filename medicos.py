import hashlib

from app import log
from dominios.db import ProfissionalSaudeModel, EstadoModel, PessoaModel, UsuarioModel, \
    PerfilUsuarioEstabelecimentoSaudeModel


class Medicos:

    # Método estático de criação do médico, é estático pois não usa self
    @staticmethod
    def cadastra_medico(sessao: 'session from sqlAlchemy', crm: 'String or int with number of crm',
                        uf: '2 digits representing UF from Brazil state', nome: 'Doctor name',
                        perfil: 'Perfil médico Solicitante ou Executor',
                        **kwargs: 'The kwargs can set signature'):
        """Function that return a ProfissionalSaudeModel"""

        # Fazemos a busca do identificador do estado
        id_uf = sessao.query(EstadoModel).filter_by(
            sigla=uf.upper()).first().identificador
        # Verificamos se em kwargs há login
        login = kwargs.get('login', None)
        # Caso não haja pressupõe-se que será Médico solicitante
        if login is None:
            login = f'{uf.lower()}{crm}'
        # Verifica se a identificador de estabelecimentos de saúde local
        identificador_estabelecimento_saude = kwargs.get(
            'identificador_estabelecimento_saude', None)
        # Caso não haja pegar pro padrão 1 isso pode atribuir erros
        if identificador_estabelecimento_saude is None:
            identificador_estabelecimento_saude = 1
        log.info('Login = %s, uf = %s, crm = %s', (login, uf, crm))
        # Fazendo uma checagem para verificar se não há nenhum
        # profissional de saúde cadastrados em pessoa model
        p_alchemy = sessao.query(PessoaModel).filter_by(nome=nome).first()
        log.info('Buscando pessoa.')
        # Fazendo checagem pra ver se não existe profissional
        # de saúde cadastrados na tabela profissional de saúde
        ps_alchemy = sessao.query(ProfissionalSaudeModel) \
            .filter_by(registro_conselho_trabalho=crm) \
            .filter(ProfissionalSaudeModel.identificador_estado_conselho_trabalho == id_uf) \
            .first()
        log.info('Buscando profissional de saude.')
        # Verificando se não à o usuário criado com o mesmo login passado nos parâmetros
        usr_alchemy = sessao.query(UsuarioModel).filter(
            UsuarioModel.login == login).first()
        log.info('Buscando usuário.')
        log.info('Verificando se existe médico cadastrado')
        # Verificando se a assinatura caso não haja pressupõe-se que
        # será médico solicitante
        assinatura = kwargs.get('assinatura', None)

        # Verifica se alguma das instâncias tanto pessoa
        # profissional de saúde é o usuário já estão existentes
        if p_alchemy or ps_alchemy or usr_alchemy:
            log.info('Usuario Já Cadastrado')

        # Caso não exista inicia-se processo de criação do usuário
        else:
            # Cria-se 1º. pessoa model
            p_novo = PessoaModel(nome=nome, ativa=True)
            log.info('Modelo de pessoa nova cadastrado')
            try:
                # Com pessoa model criado adiciona-se ao banco de dados
                sessao.add(p_novo)
                log.info('Pessoa inserida')
                sessao.commit()
                log.info('Nova pessoa commitada')
            except Exception as expc:
                log.info('Um erro ocorreu ao inserir nova pessoa.')
                log.info('Erro: %s', expc)
                log.info('Fazendo rollback()')
                sessao.rollback()
                raise Exception(f"Um erro ocorreu {expc}")

            # iniciasse agora o processo de criação do profissional de saude
            ps_novo = ProfissionalSaudeModel(
                identificador_pessoa=p_novo.identificador,
                identificador_tipo_conselho_trabalho=1,
                identificador_estado_conselho_trabalho=id_uf,
                registro_conselho_trabalho=crm,
                ativo=True)
            # Com o modelo criado verifica se existe assinatura
            if assinatura:
                # se houver assinatura atribui-se
                ps_novo.assinatura_digitalizada = assinatura
            log.info('Profissional de saude model criado')
            try:
                # persiste-se há informações no banco de dados
                sessao.add(ps_novo)
                log.info('Profissinal de saude model inserido no banco.')
                sessao.commit()
                log.info('Profissinal de saude commitado no banco.')
            except Exception as expc:
                log.info('Erro ao inserir profissinal de saude')
                log.info('Erro: %s', expc)
                log.info('Fazendo rollback')
                sessao.rollback()
                log.info('Deletando pessoal relacionada criada %s', nome)
                sessao.delete(p_novo)
                sessao.commit()
                log.info('Pessoa nova deletada.')
                raise Exception(f"Um erro ocorreu {expc}")

            # inicie o processo de criação de usuário
            usr_novo = UsuarioModel(
                login=login,
                senha=hashlib.md5(crm.encode('utf-8')).hexdigest(),
                administrador=False,
                identificador_pessoa=p_novo.identificador,
                ativo=True
            )
            try:
                # persiste-se informação no banco de dados
                log.info('Inserindo novo usuário')
                sessao.add(usr_novo)
                log.info('Novo usuário inserido')
                sessao.commit()
                log.info('Commiting novo usuário')
            except Exception as expc:
                log.info('Um erro ocorreu ao inserir novo usuário')
                log.info('Erro: %s', expc)
                log.info('Fazendo rollback')
                sessao.rollback()
                log.info('Deletando profissional de saude relacionado')
                sessao.delete(ps_novo)
                sessao.commit()
                log.info('Deletando pessoa nova')
                sessao.delete(p_novo)
                sessao.commit()
                raise Exception("Um erro ocorreu ", expc)

            # inicia-se o processo de criação de perfil usuário de saúde
            pues_novo = PerfilUsuarioEstabelecimentoSaudeModel(
                identificador_perfil=perfil,
                identificador_usuario=usr_novo.identificador,
                identificador_estabelecimento_saude=1,
                data_inicial='2020-06-01'
            )
            try:
                # A informação é persistido no banco de dados
                log.info('Adicionando novo perfil usuário.')
                sessao.add(pues_novo)
                sessao.commit()
            except Exception as expc:
                log.info('Um erro ocorreu ao inserir perfil usuário.')
                log.info('Erro: %s', expc)
                sessao.rollback()
                log.info('Deletando usuario relacionado.')
                sessao.delete(usr_novo)
                sessao.commit()
                log.info('Deletando profissional de saude relacionado')
                sessao.delete(ps_novo)
                sessao.commit()
                log.info('Deletando pessoa nova')
                sessao.delete(p_novo)
                sessao.commit()
                raise Exception(f"Um erro ocorreu {expc}")
            # Caso tudo tenha ocorrido certo retornas e profissional de saúde
            return ps_novo
