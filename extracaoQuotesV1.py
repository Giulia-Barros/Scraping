from selenium import webdriver #controla o navegador de forma automatiza
import time

#Opening the Chrome browser 
browserChrome = webdriver.Chrome()

# Opening the website
browserChrome.get("https://quotes.toscrape.com/")
browserChrome.maximize_window()

# Selecting screen element
browserChrome.find_elements("style")

time.sleep(10)