# scraping program that obtains addresses of Porsche locations in China
# can be modified to scrape other websites
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.porsche.com/china/en/dealersearch/")
driver.implicitly_wait(2)

cities = ["Hong Kong", "Wuhan", "Beijing", "Nanjing", "Shanghai"]
results = []

wait = WebDriverWait(driver, 20)

for city in cities:
    driver.refresh()
    driver.implicitly_wait(20)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "gui-search-input")))
    input_element = driver.find_element(By.CLASS_NAME, "gui-search-input")
    input_element.click()
    input_element.clear()
    input_element.send_keys(city)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "gui-link-with-arrow")))
    driver.find_element(By.CLASS_NAME, "gui-link-with-arrow").click()
    #driver.execute_script("arguments[0].click();", element)
    # driver.save_screenshot('debug_screenshot.png')

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "slick-track")))
    popup_html = driver.find_element(By.CLASS_NAME, "slick-track").get_attribute('innerHTML')
    soup = BeautifulSoup(popup_html, "lxml")
    dealer_info = soup.find_all("div", class_="m-113__dealerBox-dealerName")
    for dealer in dealer_info:
        results.append(dealer.get_text(strip=True))


for result in results:
    print(result)

