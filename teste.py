import pyautogui as pyaut

class Robo:
    def __init__(self):
        pass
    def open_browser(self):
        pyaut.press('win')
        pyaut.write('Firefox')
        pyaut.press('enter')

    def open_page(self):
        pyaut.write('https://www.gsuplementos.com.br/creatina-monohidratada-250gr-growth-supplements-p985931')
        pyaut.press('enter')

robozin = Robo()


def main():
    robozin.open_browser()
    robozin.open_page()


main()
