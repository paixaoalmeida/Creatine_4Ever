#Essa parte do código vai realizar a compra automatizada com o selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager #importando as bibliotecas necessárias para abrir o firefox


service = FirefoxService(executable_path=GeckoDriverManager().install()) #Instalando o driver de uma lib

driver = webdriver.Firefox(service=service) #criando o objeto

driver.get("https://www.linkedin.com")

driver.find_element_by_xpath("/html/body/main/section[1]/div/div/form/div[2]/button").click()

