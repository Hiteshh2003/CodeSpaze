from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

def scrape_dynamic_site():
    # Setup WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = "https://quotes.toscrape.com/js/"
    driver.get(url)

    # Allow the page to load
    time.sleep(3)
    
    quotes = []
    quote_elements = driver.find_elements(By.CLASS_NAME, "quote")
    for quote_elem in quote_elements:
        text = quote_elem.find_element(By.CLASS_NAME, "text").text
        author = quote_elem.find_element(By.CLASS_NAME, "author").text
        quotes.append({"text": text, "author": author})
    
    save_to_csv(quotes, "quotes.csv")
    driver.quit()
    print("Data scraped and saved successfully!")

def save_to_csv(data, filename):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["text", "author"])
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    scrape_dynamic_site()
