# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2:Fazer Login
# Pasoo 3: Importar a Base de dados
# Passo 4: Cadastrar um Produto
# Passo 5: repetir o processo de cadastro até acabar


# Passo 1:
import pyautogui
import time # biblioteca que tem o comando sleep para dar um delay em comandos especificos


pyautogui.PAUSE = 1 # dar delay entre todos os comandos
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever texto
# pyautogui.press -> pressionar 1 tecla do teclado
# pyautogui.hotkey -> pressionar uma combinação de teclas

# abrir o navegador

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter") 

time.sleep(0.5)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(1)

# Passo 2: logar
pyautogui.click(x=657, y=484)
pyautogui.write("gabrielo@hotmai.com")

time.sleep(1)

# escrever senha
pyautogui.press("tab")
pyautogui.write("1111111111")

#clicar no botao de logar
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# Passo 3: importar a base de dados
# pip install pandas numpy openpyx1

import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

#passo 4 cadastrar
for linha in tabela.index:
    #clica no primeiro campo
    pyautogui.click(x=717, y=397)

    #codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab") 

    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab") 

    #categotia

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab") 

    #preço
   
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab") 

    #custo
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab") 

    #obs
    obs = tabela.loc[linha, "obs"]
    if  not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab") 

    #enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)       


    # str serve para tranformar os numeros em texto
