import pyautogui
import time
import pandas as pd
pyautogui.PAUSE = 1.3

# abrir o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# acessar o sistema: dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write('dlp.hashtagtreinamentos.com/python/intensivao/login')
time.sleep(2)
pyautogui.press('enter')
time.sleep(3)

# fazer login
pyautogui.press('tab')
pyautogui.write('giulliano@gmail.com')
pyautogui.press('tab')  
pyautogui.write('senha')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)
# carregar base de dados
tabela = pd.read_csv('c:/Users/giull/Desktop/Projetos GIT/Automação Cadastro/produtos.csv')
# cadastrar produto e repetir processo
pyautogui.PAUSE = 0.5
for linha in tabela.index:
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    if not pd.isna(tabela.loc[linha, 'obs']):
        pyautogui.write(str(tabela.loc[linha, 'obs']))
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('pageup')
    pyautogui.click(x=99, y=237)