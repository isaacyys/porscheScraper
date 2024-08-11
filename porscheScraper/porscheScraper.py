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

# I can modify this such that it parses a CSV containing the city names as well
cities = ["Hong Kong", "Beijing", "Nanjing"]
results = []
results1 = []
results2 = []
results3 = []

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

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "slick-track")))
    popup_html = driver.find_element(By.CLASS_NAME, "slick-track").get_attribute('innerHTML')
    soup = BeautifulSoup(popup_html, "lxml")
    dealer_info = soup.find_all("div", class_="m-113__dealerBox-dealerName")
    for dealer in dealer_info:
        results.append(dealer.get_text(strip=True))
    dealer_street = soup.find_all("div", class_="street")
    for dealer in dealer_street:
        results1.append(dealer.get_text(strip=True))
    dealer_code = soup.find_all("span", class_="postCode")
    for dealer in dealer_code:
        results2.append(dealer.get_text(strip=True))
    dealer_city = soup.find_all("span", class_="city")
    for dealer in dealer_city:
        results3.append(dealer.get_text(strip=True))


for result in results:
    print(result)
for result in results1:
    print(result)
for result in results2:
    print(result)
for result in results3:
    print(result)
