import requests
from html2text import html2text
import datetime
from credentials import CREDENTIALS

identificador_estabelecimento_saude = 49
url_laudo = f'http://sistema.elaudos.com/api/laudos/{identificador_estabelecimento_saude}'
url_estudo = 'http://sistema.elaudos.com/api/estudo/%s'
url_profissional = 'http://sistema.elaudos.com/api/profissional/%s'
url_login = 'http://sistema.elaudos.com/api/login'

cred = CREDENTIALS

make_login = requests.post(url=url_login, json=cred)
token = make_login.json()['access_token']
print(token)

head = {'Authorization': 'Bearer ' + token}

response_laudos = requests.get(url=url_laudo, headers=head)

laudos = response_laudos.json()

for laudo in laudos:

    data_hora_emissao = laudo['data_hora_emissao']
    data_hora_revisao = laudo['data_hora_revisao']
    identificador = laudo['identificador']
    identificador_estudo_dicom = laudo['identificador_estudo_dicom']
    integrado = laudo['integrado']
    numero_exames_relacionados = laudo['numero_exames_relacionados']
    situacao = laudo['situacao']
    situacao_envio_his = laudo['situacao_envio_his']
    texto = laudo['texto']
    identificador_profissional_saude = laudo['identificador_profissional_saude']

    response_estudo = requests.get(
        url=url_estudo % identificador_estudo_dicom, headers=head)
    estudo = response_estudo.json()
    
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

    profissional_s = requests.get(url=url_profissional %identificador_profissional_saude, headers=head) 
    profissional_s = profissional_s.json()
    profissional = profissional_s['']