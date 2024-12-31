import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/explorer/crime/query")

dataset = driver.find_element(By.XPATH, '//*[@id="dataset-select-query"]/button/span')
dataset.click()

driver.find_element(By.XPATH, '//*[@id="nb-option-0"]').click()

querylevelb = driver.find_element(By.XPATH, "//button/span[normalize-space(text())='Query Level']")
querylevelb.click()
driver.find_element(By.XPATH, '//*[@id="nb-option-1"]').click()

crime = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button/span[normalize-space(text())='Crime(s)']")))

crime.click()

crime_id = 2
driver.find_element(By.XPATH, f'//nb-option[{crime_id}]').click()

location = driver.find_element(By.XPATH,"//button/span[normalize-space(text())='Location']")
location.click()

loc_id = 2
driver.find_element(By.XPATH, f'//nb-option[{loc_id}]').click()
time.sleep(5)
