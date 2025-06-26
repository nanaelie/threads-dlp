import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

def extractor(url: str) -> (bool, str):
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    try:
        video = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "video"))
        )
        video_url = video.get_attribute("src")
        return True, video_url
    except:
        return False, "No video found!"
    
    finally:
        driver.quit()
    
        
    
