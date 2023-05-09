#Código iniciado no dia 1 de maio
#LIBRARIES------------------------------------------LIBRARIES-------------------------------LIBRARIES
import time
import Selenium_buy as Robot_buy #importando o arquivo do selenium que realiza a compra
import keys #Importando as informações de login do Twilio de um arquivo no mesmo repositório
import os
from requests_html import HTMLSession
from twilio.rest import Client
from datetime import datetime
from time import sleep

#FUNÇÕES---------------------------------------FUNÇÕES------------------------------------------FUNÇÕES
def SendMessage(): #Função send_email com a API do Twilio
    client = Client(keys.account_sid, keys.auth_token)

    message = client.messages \
        .create(
        body='Creatina Creapure está disponível! Estamos comprando pra você, se não deu certo, compre manualmente no link: https://www.gsuplementos.com.br/creatina-250g-creapure-growth-supplements-p985824',
        from_=keys.twilio_number,
        status_callback='https://abc1234.free.beeceptor.com',
        to=keys.target_number
    )

    print(message.sid)

def CheckCreatine():
        global text_list #Definindo uma váriavel global pra eu poder usar ela fora de função (vai virar uma array)

        session = HTMLSession()  # Objeto com a função da lib
        r = session.get('https://www.gsuplementos.com.br/creatina-250g-creapure-growth-supplements-p985824')

        r.html.render(sleep=5)  # Renderiza o JavaScript da página

        comp = r.html.find('.botao-de-compra > div:nth-child(1) > a:nth-child(1) > button:nth-child(1)',first=True)  # A primeira que achar, vai te dar, caso contrário, vai dar uma lista e vai dar erro

        text = comp.text  # Retorna o texto do elemento que vc marcou
        text_list = [text] #Coloca o resultado do texto numa lista

def BuyS():
    print("Efetuando a compra da Creatina em " + str(datetime) + "....")
    Robot_buy.BuyCreatine


#CÓDIGO--------------------------------------CÓDIGO-------------------------------------CÓDIGO------
if __name__ == "__main__":
    big_loop = True
    while big_loop:
        CheckCreatine() #Roda a função para verificar a disponibilidade


        loop = True #Variável para usar como uma flag no loop
        while loop:
            if 'AVISE-ME QUANDO CHEGAR' in text_list: #Se um dos dados parseados estiver dessa maneira, não tem disponível
                print("NÃO DISPONÍVEL! " + str(datetime.now())) #Printa o horário para fins de registro
                time.sleep(120) #Como é um código para monitoramento, se o produto não estiver disponível, aguarda um pouco e volta tudo novamente
                CheckCreatine() #Volta a função para verificar a disponibilidade
            elif 'AVISE-ME QUANDO CHEGAR' not in text_list: #Caso contrário, aparece 'comprar', então pode enviar o e-mail
                SendMessage() and BuyS #Função que envia o sms
                big_loop = False
                exit(0)
