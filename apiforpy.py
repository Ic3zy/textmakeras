from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
app = Flask(__name__)

@app.route('/photooxy', methods=['GET'])
def photooxy():
    user_text = request.args.get('text')
    target_url = request.args.get('url')

    if not target_url:
        return jsonify({'status': 'error', 'message': 'URL is required'}), 400
    chrome_options = Options()
    #chrome_options.add_argument('--headless')  # Headless modda çalıştır
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(), options=chrome_options)

    try:
        driver.get(target_url)
        script = f"""
        const inputText = document.querySelector('input[name="text[]"]'); 

        inputText.value = "{user_text}";

        const submitButton = document.querySelector('input[type="submit"]'); 
        submitButton.click(); // Butona tıkla
        """
        driver.execute_script(script) 
        link_image_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'link-image')) 
        )
        sleep(2)
        link_image_text = link_image_element.text
        return jsonify({'link_image_text': link_image_text})
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})
    
    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
