from time import sleep

import pyperclip
import pyautogui as pyaut


class Robo:
    def __init__(self):
        pass
    def open_browser(self) -> None:
        pyaut.press('win')
        pyaut.write('Firefox')
        pyaut.press('enter')

    def open_purchase_page(self) -> None:
        pyperclip.copy('https://www.gsuplementos.com.br/creatina-monohidratada-250gr-growth-supplements-p985931')
        sleep(2)
        pyaut.hotkey('ctrl', 'v')
        sleep(1)
        pyaut.press('enter')
        sleep(10)
        for i in range(0, 28):
            pyaut.press('tab')
        pyaut.press('enter')

    def fill_cpf_and_cupom(self, *, cep: str, cupom: str) -> None:
        sleep(6)
        for i in range(0, 15):
            pyaut.press('tab')
        pyaut.write(cep)
        pyaut.press('tab')
        pyaut.press('enter')

        sleep(6)
        for i in range(0, 3):
            pyaut.press('tab')
        pyaut.write(cupom)
        pyaut.press('tab')
        pyaut.press('enter')

        for i in range(0, 31):
            pyaut.press('tab')
        pyaut.press('enter')

    def finish_purchase(self, *, senha: str) -> None:
        for i in range(0, 2):
            pyaut.press('tab')
        pyaut.write('almeidapaixao04@gmail.com')
        sleep(5)
        pyperclip.copy(senha)
        sleep(3)
        pyaut.hotkey('ctrl', 'v')


robozin = Robo()


def main():
    robozin.open_browser()
    robozin.open_purchase_page()
    robozin.fill_cpf_and_cupom(cep='05333090', cupom='JASON')
    robozin.finish_purchase(senha='B4n$#!987')


main()
