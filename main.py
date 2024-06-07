from deep_translator import GoogleTranslator
from selenium import webdriver
import time
from bs4 import BeautifulSoup

browser = webdriver.Firefox()
html = browser.page_source
soup = BeautifulSoup(html, features="html.parser")

browser.get('https://genius.com/Rolo-tomassi-contretemps-lyrics')
time.sleep(4)
grabbed_text = soup.find("div", {"class": "data-lyrics-container"})
print(grabbed_text)


selected_text = str(input("Enter the text you would like to translate:"))

translator = GoogleTranslator(source='auto', target='french')
result = translator.translate(text=selected_text)
print(result)
