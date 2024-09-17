import time
from time import sleep
import pandas as pd

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

from selenium import webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://monkeytype.com/')

from selenium.webdriver.common.by import By
popup = driver.find_element(By.XPATH, '//div[@class="buttons"]')
pop_btns = popup.find_elements(By.TAG_NAME, 'button')
pop_btns[0].click()
sleep(5)

from selenium.webdriver.common.keys import Keys
input_wrapper = driver.find_element(By.XPATH, '//div[@id="wordsWrapper"]')
input_letters = input_wrapper.find_element(By.TAG_NAME, 'input')
sleep(0.5)

start_time = time.time()
timeout = 30

while True:
    current_time = time.time()
    if current_time - start_time > timeout:
        print("Tempo limite alcançado, saindo do loop.")
        break

    wrds_div = driver.find_element(By.XPATH, '//div[@id="words"]')
    wrd = wrds_div.find_element(By.XPATH, '//div[@class="word active"]')

    letters = ''.join(wrd.text)
    letters += ' '

    for letter in letters:
        # print(letter, end="", flush=True)
        input_letters.send_keys(letter)
        # sleep(0.05)

sleep(60)
driver.close()