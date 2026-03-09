# Passo 1: Abrir o sistema da empresa
# Passo 2: Fazer o login
# Passo 3: Abrir o sistema de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o passo 4 ate acabar a lista de produtos

import os
import time

import pandas
import pyautogui

pyautogui.PAUSE = 0.5

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL", "seu_email@exemplo.com")
LOGIN_SENHA = os.getenv("LOGIN_SENHA", "")

# pyautogui.click - clica
# pyautogui.write - escreve
# pyautogui.press - pressiona
# pyautogui.hotkey - atalho
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

# Fazer uma pausa maior para abrir o site
time.sleep(3)
pyautogui.click(x=669, y=667)
pyautogui.write(LOGIN_EMAIL)
pyautogui.press("tab")
pyautogui.write(LOGIN_SENHA)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(5)

# Login concluido

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # Cadastrar 1 produto
    pyautogui.click(x=650, y=520)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(6000)
