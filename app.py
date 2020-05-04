import requests
from html2text import html2text
import datetime
from credentials import CREDENTIALS

identificador_estabelecimento_saude = 48
url_laudo = f'http://sistema.elaudos.com/api/laudos/{identificador_estabelecimento_saude}'
url_login = 'http://sistema.elaudos.com/api/login'

cred = CREDENTIALS

make_login = requests.post(url=url_login, json=cred)
token = make_login.json()['access_token']
print(token)

head = {'Authorization': 'Bearer ' + token}

response_laudos = requests.get(url=url_laudo, headers=head)

laudos = response_laudos.json()

for laudo in laudos:
    texto = html2text(laudo['texto']).replace('\\', '').replace(
        '*', '').replace(' Ó', 'Ó')
    data_emissao = laudo['data_hora_emissao'].split('T')[0].replace('-', '')
    hora_emissao = laudo['data_hora_emissao'].split('T')[1].split('.')[
        0].replace(':', '')
    accessionnumber = laudo['estudo_dicom']['accessionnumber']
    arquivo_xml = open(
        f"D:/XML-Laudos/{data_emissao}-{hora_emissao}-{accessionnumber}.XML", "a")
    arquivo_laudo_texto = open(
        f"D:/Laudos/{data_emissao}-{hora_emissao}-{accessionnumber}.txt", "a")
    arquivo_laudo_texto.write(texto)
    arquivo_laudo_texto.close()

    xml = f"""
    <?xml version="1.0" encoding="utf-8"?>
    <DATAPACKET Version="2.0">
        <ROWDATA>
            <Operation>I</Operation>
            <AccessionNumber>{accessionnumber}</AccessionNumber>
            <ReportFolder>D:\Laudos\</ReportFolder>
            <ReportName>{data_emissao}-{hora_emissao}-{accessionnumber}.txt</ReportName>
            <Radiologist>{laudo['executor_laudo']['pessoa']['nome']}</Radiologist>
            <MDLicense>{laudo['executor_laudo']['registro_conselho_trabalho']}</MDLicense>
            <State>{laudo['executor_laudo']['estado_conselho_trabalho']['nome']}</State>
        </ROWDATA>
    </DATAPACKET>
    """

    arquivo_xml.write(xml)
    arquivo_xml.close()

    indetificador_laudo = laudo['identificador']
    url_to_put = f'http://sistema.elaudos.com/api/laudo/{indetificador_laudo}'
    print(url_to_put)
    integra = requests.put(
        url=url_to_put, headers=head)
    print(integra.status_code)
