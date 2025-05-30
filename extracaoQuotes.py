import pandas as pd

from selenium import webdriver #controla o navegador de forma automatiza
from selenium.webdriver.chrome.service import Service #inicializa o ChromeDriver
from selenium.webdriver.common.by import By #localiza os elementos da página html
#import time

#INSTÂNCIA DO CHROME

#Cria o objeto Service que é utilizado para iniciar o ChromeDrive
service = Service()

# Cria um objeto ChromeOptions que permite configurar opções do navegador (ex.: idioma)
options = webdriver.ChromeOptions()

# Abre uma janela no navegador com as configurações especificadas
browser = webdriver.Chrome(service=service, options=options)
#browser.maximize_window()

url = "https://quotes.toscrape.com/"
browser.get(url)

#time.sleep(10)

#ENCONTRANDO

# Buscando pela tag
#find_element(By.TAG_NAME, "nome da tag")
# Buscando pela classe
#find_element(By.CLASS_NAME, "nome classe")

# Frases
# frases = browser.find_elements(By.CLASS_NAME, "text")

# # Imprimir o texto de todos os links
# for f in frases:
#     text = f.text.strip()
#     print(text)

# # Autor
# autor = browser.find_elements(By.CLASS_NAME, "author")

# for a in autor:
#     text = a.text.strip()
#     print(text)

# ## Tags
# tag = browser.find_elements(By.CLASS_NAME, "tag")

# for t in tag:
#     text = t.text.strip()
#     print(text)



browser.quit()