#Código iniciado no dia 1 de maio | O objetivo é fazer funcionar e depois começar a realizar atividades complexas com ele

from requests_html import HTMLSession

def CheckCreatine():
    global text_list #Definindo uma váriavel global pra eu poder usar ela fora de função (vai virar uma array)

    session = HTMLSession()  # Objeto com a função da lib
    r = session.get('https://www.gsuplementos.com.br/creatina-250g-creapure-growth-supplements-p985824')

    r.html.render(sleep=3)  # Renderiza o JavaScript da página

    comp = r.html.find('.botao-de-compra > div:nth-child(1) > a:nth-child(1) > button:nth-child(1)',first=True)  # A primeira que achar, vai te dar, caso contrário, vai dar uma lista e vai dar erro

    text = comp.text  # Retorna o texto do elemento que vc marcou
    text_list = [text] #Coloca o resultado do texto numa lista

def CheckSum():
    if 'AVISE-ME QUANDO CHEGAR' in text_list:
        print("TÁ SEM!") #Dá um timer de alguns minutos, e verifica novamente (futuramente)
    elif 'AVISE-ME QUANDO CHEGAR' not in text_list:
        print("VEM COMPRAR PAPAI!") #Vai ser enviado um e-mail


CheckCreatine()
CheckSum()
