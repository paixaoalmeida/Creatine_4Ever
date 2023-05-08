#Essa parte do código vai realizar a compra automatizada com o selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager #importando as bibliotecas necessárias para abrir o firefox

service = FirefoxService(executable_path=GeckoDriverManager().install()) #Instalando o driver de uma lib

driver = webdriver.Firefox(service=service) #criando o objeto

driver.get("https://www.gsuplementos.com.br/creatina-250g-creapure-growth-supplements-p985824")

time.sleep(10)

driver.maximize_window #maximixe windows

elem = driver.find_element('xpath' , '//*[@id="wCookieConsentBar-acceptAll"]')

elem.send_keys(Keys.ENTER)

buy = driver.find_element('xpath', '/html/body/main/section[3]/div/div[3]/div/div[3]/div/a/button' )

buy.send_keys(Keys.ENTER)

time.sleep(5)

cart = driver.find_element('xpath' , '//*[@id="finalizarPedido"]').send_keys(Keys.ENTER)

time.sleep(5)

cep = driver.find_element('xpath', '/html/body/main/section[2]/div/div[9]/div[4]/div[1]/div/div[1]/form/div/input').send_keys('05333090')

time.sleep(5)

cupom = driver.find_element('xpath', '/html/body/main/section[2]/div/div[9]/div[4]/div[2]/div/div/form/div/input').send_keys('GIGA')

time.sleep(5)

close_buy = driver.find_element('xpath', '/html/body/main/section[2]/div/div[10]/div/div[1]/div/div[2]/a[2]/button').send_keys(Keys.ENTER)

time.sleep(5)

email = driver.find_element('xpath', '/html/body/main/section/div/div[1]/div/div[2]/div/form/div[1]/div[1]/input').send_keys('almeidapaixao04@gmail.com')

time.sleep(5)

continue_button = driver.find_element('xpath', '/html/body/main/section/div/div[1]/div/div[2]/div/form/div[3]/div[1]/button').send_keys(Keys.ENTER)

time.sleep(5)

passwd = driver.find_element('name', 'senha').send_keys('B4n$#!987')

time.sleep(5)

continue_after_passwd = driver.find_element('xpath', '/html/body/main/section/div/div[1]/div/div[2]/div/form/div[3]/div[1]/button').send_keys(Keys.ENTER)

time.sleep(5)

go_payment = driver.find_element('xpath', '/html/body/main/section[2]/div/div[1]/div/div[2]/div/div[3]/div[2]/a/div/button').send_keys(Keys.ENTER)

time.sleep(5)

pix = driver.find_element('css selector', 'div.mainBox-conteudo-formasPag-opcao:nth-child(3)')

pix.click()

time.sleep(5)

#end_purchase = driver.find_element('css selector', '#formPagamentoPix > div:nth-child(6) > button:nth-child(1)')

#end_purchase.click
element = driver.find_element('css selector', '#formPagamentoPix > div:nth-child(6) > button:nth-child(1)')
driver.execute_script("$(arguments[0]).click();", element) #Use some java to click the element


