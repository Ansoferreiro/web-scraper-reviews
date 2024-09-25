# backend/scraper.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import json

def scrape_reviews():
    # Inicializando o driver com o caminho do ChromeDriver
    service = Service(r"C:\Users\Wanderson Ferreira\Documents\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.amazon.com/product-reviews/YOUR_PRODUCT_ID")

    time.sleep(3)  # Esperar a página carregar

    reviews = driver.find_elements(By.CSS_SELECTOR, ".review-text-content span")
    review_list = [review.text for review in reviews]

    driver.quit()
    return review_list

if __name__ == "__main__":
    print(json.dumps(scrape_reviews()))


