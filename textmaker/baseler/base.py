# Coded By @Ic3zy
# Copyright (C) 2024 Ic3zy.

# Licensed under the  GPL-3.0 License;
# you may not use this file except in compliance with the License.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import os
# def path_driverbyc(chrome_driver_path):
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     service = Service(chrome_driver_path)
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#     return driver
def download_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            file.write(response.content)
    except requests.RequestException as e:
        print(f"Görsel Üretme Hatası. {e} : By Owner Ic3zy")
def ttp(driver, text, flmlnk, save_path="C:\\Program Files"):
    chrome_driver_path=f"{driver}"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        url = f'{flmlnk}?text={text}'
        url = url.replace(" ", "%20")
        print(url)
        driver.get(url)       
        image_element = driver.find_element(By.ID, 'logoImage-1')
        image_url = image_element.get_attribute('src')
        print("Görsel Üretildi: By Owner Ic3zy")
        if not image_url:
            print("Görsel Üretilemedi Lütfen Bir Süre Sonra Tekrar Dene : By Owner Ic3zy")
            return
        download_image(image_url, save_path)
    finally:
        print("driver.quit()")
def close(driver):
    driver.quit()
