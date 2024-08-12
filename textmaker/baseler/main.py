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
# geckodriver_path = 'geckodriver\\geckodriver.exe' 
# firefox_options = Options()
# firefox_options.add_argument("--headless")
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
        print(f"Görsel başarıyla indirildi. {save_path} : By Owner Ic3zy")
    except requests.RequestException as e:
        print(f"Görsel indirme hatası. {e} : By Owner Ic3zy")
def textbase(geckodriver,text, url, save_path="download\\ttp.jpg"):
    geckodriver_path = f'{geckodriver}' 
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    try:
        service = Service(executable_path=geckodriver_path)
        driver = webdriver.Firefox(service=service, options=firefox_options)
        driver.get(url)
        wait = WebDriverWait(driver, 20)
        element = wait.until(EC.presence_of_element_located((By.NAME, 'text[]')))
        textbutton = driver.find_element(By.NAME, "text[]")
        textbutton.send_keys(text)
        textbutton.send_keys(Keys.RETURN)
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='thumbnail']//img")))
        time.sleep(1.2)
        image_element = driver.find_element(By.XPATH, "//div[@class='thumbnail']//img")
        time.sleep(4)
        image_url = image_element.get_attribute('src')
        if not image_url:
            print("Görsel URL'si bulunamadı : By Owner Ic3zy")
            return
        download_image(image_url, save_path)
        def close():
            driver.quit()
    finally:
        #driver.quit()
        pass
def close():
    exit()