import pyautogui
import time
import pandas as pd

# Pausa  de 2s para o PyAutoGUI
pyautogui.PAUSE = 1.3

# Carregar base de dados
CAMINHO_ARQUIVO_CSV = 'c:/Users/giull/Desktop/Projetos GIT/Automação Cadastro/produtos.csv'

# Fazer login
def fazer_login(email, senha):
    pyautogui.press('tab')
    pyautogui.write(email)
    pyautogui.press('tab')  
    pyautogui.write(senha)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(2)

# Preencher os dados do produto
def preencher_dados_produto(produto):
    pyautogui.press('tab')
    pyautogui.write(str(produto['codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(produto['marca']))
    pyautogui.press('tab')
    pyautogui.write(str(produto['tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(produto['categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(produto['preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(produto['custo']))
    pyautogui.press('tab')
    if not pd.isna(produto['obs']):
        pyautogui.write(str(produto['obs']))
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(1)

# Carregar base de dados
tabela = pd.read_csv(CAMINHO_ARQUIVO_CSV)

# Abrir navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# Acessar o sistema: dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write('dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)

# Fazer login
fazer_login('giullianoveiga@gmail.com', 'senha')

# Cadastrar produtos e repetir o processo
pyautogui.PAUSE = 0.5
for _, produto in tabela.iterrows():
    preencher_dados_produto(produto)
    pyautogui.press('pageup')
    pyautogui.click(x=99, y=237)
