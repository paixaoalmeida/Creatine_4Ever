#Código iniciado no dia 1 de maio

import keys #Importando as informações de login do Twilio de um arquivo no mesmo repositório
import os
from requests_html import HTMLSession
from twilio.rest import Client

def SendMessage(): #Função send_message com a API do Twilio
    client = Client(keys.account_sid, keys.auth_token)

    message = client.messages \
        .create(
        body='Creatina está disponível! https://www.gsuplementos.com.br/creatina-250g-creapure-growth-supplements-p985824',
        from_=keys.twilio_number,
        status_callback='https://abc1234.free.beeceptor.com',
        to=keys.target_number
    )

    print(message.sid)
    
def CheckCreatine():
    global text_list #Definindo uma váriavel global pra eu poder usar ela fora de função (vai virar uma array)

    session = HTMLSession()  # Objeto com a função da lib
    r = session.get('https://www.gsuplementos.com.br/creatina-250g-creapure-growth-supplements-p985824')

    r.html.render(sleep=3)  # Renderiza o JavaScript da página

    comp = r.html.find('.botao-de-compra > div:nth-child(1) > a:nth-child(1) > button:nth-child(1)',first=True)  # A primeira que achar, vai te dar, caso contrário, vai dar uma lista e vai dar erro

    text = comp.text  # Retorna o texto do elemento que vc marcou
    text_list = [text] #Coloca o resultado do texto numa lista


CheckCreatine() #Roda a função para verificar a disponibilidade


if 'AVISE-ME QUANDO CHEGAR' in text_list: #Se um dos dados parseados estiver dessa maneira, não tem disponível
    print("TÁ SEM!")
    exit(0)
elif 'AVISE-ME QUANDO CHEGAR' not in text_list: #Caso contrário, aparece 'comprar', então pode enviar o e-mail
    SendMessage() #Função que envia o sms

