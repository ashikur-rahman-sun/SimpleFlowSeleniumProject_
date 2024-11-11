import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

json_file_path = os.path.join('data', 'attributeList.json')

with open(json_file_path, 'r') as file :
    data = json.load(file)

searchItems = data["searchItems"]

service = Service("F:\Study\seleniumFiles\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://google.com")
print(driver.title)

# Wait for Google search bar to be present and interact with it
WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)
input_element = driver.find_element(by=By.CLASS_NAME, value="gLFyf")
input_element.click()
input_element.send_keys("tech with tim" + Keys.ENTER)

# Wait for "Tech With Tim" link to appear and click on it
WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
)
link = driver.find_elements(by=By.PARTIAL_LINK_TEXT, value="Tech With Tim")
if link:
    link[0].click()

print("Launch the desired YouTube channel")
time.sleep(5)
print("Waiting for the YouTube Channel Name:", driver.current_url)
WebDriverWait(driver, 10).until(
    EC.url_contains("youtube.com")
)
print("On YouTube!")

# Wait for the YouTube search bar to be clickable and interact with it
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div["
                                          "2]/ytd-searchbox/form/div[1]/div[1]/input"))
)

search_bar = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div["
                                           "2]/ytd-searchbox/form/div[1]/div[1]/input")

for i, searchItem in enumerate(searchItems, start=1):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div["
                                              "2]/ytd-searchbox/form/div[1]/div[1]/input"))
    )

    # Click and search
    search_bar.click()
    search_bar.clear()
    search_bar.send_keys(searchItem + Keys.ENTER)

    print(f"Search {i} - Searching for '{searchItem}'")
    time.sleep(3)

driver.quit()
