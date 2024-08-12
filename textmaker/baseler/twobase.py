# Coded By @Ic3zy
# Copyright (C) 2024 Ic3zy.

# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.

# Text-Maker - Ic3zy

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time
geckodriver_path = 'geckodriver\\geckodriver.exe'
firefox_options = Options()
firefox_options.add_argument("--headless")
def download_image(image_url, save_path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://textpro.me/'
    }
    try:
        response = requests.get(image_url, headers=headers)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Görsel başarıyla indirildi: {save_path}: By Owner Ic3zy")
    except requests.RequestException as e:
        print(f"Görsel indirme hatası: {e}: By Owner Ic3zy")
def twofbase(text,text2, url, save_path="download\\ttp.jpg"):
    try:
        service = Service(executable_path=geckodriver_path)
        driver = webdriver.Firefox(service=service, options=firefox_options)
        driver.get(url)
        print("Api Sitesine Girildi: By Owner Ic3zy")
        wait = WebDriverWait(driver, 25)
        #element = wait.until(EC.presence_of_element_located((By.XPATH, """//input[@id='text-0']""")))
        time.sleep(2)
        textbutton = driver.find_element(By.XPATH, """//input[@id='text-0']""")
        twotextbutton=driver.find_element(By.XPATH, """//*[@id="text-1"]""")
        print("Elementler Yüklendi: By Owner Ic3zy")
        textbutton.send_keys(text)
        twotextbutton.send_keys(text2)
        time.sleep(0.1)
        twotextbutton.send_keys(Keys.RETURN)
        #verify=driver.find_element(By.ID, "create_effect") #Keys.RETURN işe yaramaz ise
        #verify.click()
        print("Key Girildi: By Owner Ic3zy")
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='thumbnail']//img")))
        time.sleep(1.2)
        image_element = driver.find_element(By.XPATH, "//div[@class='thumbnail']//img")
        time.sleep(5)
        image_url = image_element.get_attribute('src')
        if not image_url:
            print("Görsel URL'si bulunamadı : By Owner Ic3zy")
            return
        download_image(image_url, save_path)
    finally:
        pass
def close():
    exit()