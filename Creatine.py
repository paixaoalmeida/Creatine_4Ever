import time
import os
from time import sleep
from datetime import datetime

import pywhatkit
from requests_html import HTMLSession


def send_message():
    """Send message via WhatsApp

    This function uses the pywhatkit lib to
    send messages via WhatsApp to the sender

    Here, in order to be able to fit the requirements
    of pywhatkit, we have to put the hour and minute as integers
    with no zero before, so i converted these in the variables now_hour
    and now_min

    Since it's also recommended by the library to wait a little before
    sendind the message, we add 3 minutes more to send the message"""

    link_creatine = 'https://www.gsuplementos.com.br/creatina-250g-creapure-growth-supplements-p985824'

    now_hour = datetime.strptime(str(datetime.now()), '%Y-%m-%d %H:%M:%S.%f').strftime('%-H')
    now_min = datetime.strptime(str(datetime.now()), '%Y-%m-%d %H:%M:%S.%f').strftime('%-M')

    pywhatkit.sendwhatmsg('+5511984218991', f'Creatina disponivel!\n {link_creatine}', int(now_hour), int(now_min) + 3)


def check_creatine() -> list:
        """Aqui abrimos a página e carregamos o javascript da página
        com a funcao html.find nós monitoramos o botão de compra da creatina
        
        Retornamos a array text_list para a função abaixo usar ela na
        verificação"""
        session = HTMLSession()
        r = session.get('https://www.gsuplementos.com.br/creatina-250g-creapure-growth-supplements-p985824')


        r.html.render(sleep=5)          #Rendering the JavaScript page


        comp = r.html.find('.botao-de-compra > div:nth-child(1) > a:nth-child(1) > button:nth-child(1)',first=True)
        #A primeira que achar, vai te dar, caso contrário, vai dar uma lista e vai dar erro


        text = comp.text
        text_list: list = [text]            #Var containing the response of the scrapping at the button

        return text_list


def do_stuff(text_list:list) -> None:
    """Here we just do some simple if-else
    verification
    
    If the button is not with the AVISE ME
    QUANDO CHEGAR, then its available
    """
    while True:
        if 'AVISE-ME QUANDO CHEGAR' in text_list: 
            print("NÃO DISPONÍVEL! " + datetime.strptime(str(datetime.now()),'%Y-%m-%d %H:%M:%S.%f').strftime('%d/%m %H:%M'))
            time.sleep(120) 
        elif 'AVISE-ME QUANDO CHEGAR' not in text_list: 
            send_message()
            exit()


def main():
    """Main function of the script

    All functions of the programm are run here"""
    text_list = check_creatine()
    do_stuff(text_list)


main()