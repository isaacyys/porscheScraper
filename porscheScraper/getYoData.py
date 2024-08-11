import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.marklines.com/en/vehicle_sales/search_country/search/?searchID=3119083")

wait = WebDriverWait(driver, 10)

time.sleep(40)
driver.switch_to.window(driver.window_handles[1])

wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "aggregate_header")))

page = driver.page_source

soup = BeautifulSoup(page, "lxml")
table = soup.find_all("td", class_="aggregate_column")

counter = 0
results = []

for data in table:
    cleaned_data = [item.strip().replace('\n', '').replace('\t', '') for item in data]
    excel_ready_output = '\t'.join(cleaned_data)
    results.append(excel_ready_output)
    counter += 1
    if counter % 6 == 0:
        print(results)
        results = []

