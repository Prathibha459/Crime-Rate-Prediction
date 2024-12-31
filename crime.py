import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

driver = webdriver.Chrome()

driver.get("https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/explorer/crime/query")

time.sleep(2)

btn = driver.find_element(By.XPATH, "//button/span[normalize-space(text())='Dataset']")
btn.click()

driver.find_element(By.XPATH, "//nb-option[normalize-space(text())='Crime Data']").click()

btn1 = driver.find_element(By.XPATH, "//button/span[normalize-space(text())='Query Level']")
btn1.click()

driver.find_element(By.XPATH, '//nb-option[normalize-space(text())="National or State"]').click()

st = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California']
c = ['Homicide', 'Rape', 'Robbery']

df = {'State': [], 'Years': [], 'Homicides': [], 'Rape': [], 'Robbery': []}

state_ind = 2
for k in range(len(st)):
    crime_ind = 2
    crime = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button/span[normalize-space(text())='Crime(s)']")))

    crime.click()

    crime_select = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//nb-option[{crime_ind}]')))
    crime_select.click()

    crime_ind += 1

    loc = driver.find_element(By.XPATH, "//button/span[normalize-space(text())='Location']")
    loc.click()

    state_select = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//nb-option[{state_ind}]')))
    state_select.click()

    add_query = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[normalize-space(text())="Add Query"]'))
    )

    for i in range(2):
        add_query.click()
        crime.click()
        crime_selectt = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//nb-option[{crime_ind}]')))
        crime_selectt.click()
        loc.click()
        state_select.click()
        crime_ind += 1

    submit = driver.find_element(By.XPATH, '//button[normalize-space(text())="Submit"]')
    submit.click()

    time.sleep(2)

    table_btn = driver.find_element(By.XPATH, "//a/span[normalize-space(text())='Table']")
    table_btn.click()

    table_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a/span[normalize-space(text())='Table']"))
    )
    table_btn.click()

    for i in range(1, 12):
        year_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//tr[{i}]/td[1]'))
        )
        homi_crime = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//tr[{i}]/td[2]'))
        )
        rp = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//tr[{i}]/td[3]'))
        )
        rb = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//tr[{i}]/td[4]'))
        )
        year = year_element.text
        df['State'].append(st[k])
        df['Years'].append(year)
        df['Homicides'].append(homi_crime.text)
        df['Rape'].append(rp.text)
        df['Robbery'].append(rb.text)

    reset = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[normalize-space(text())="Reset"]'))
    )
    reset.click()

    state_ind += 1

    time.sleep(2)

d = pd.DataFrame(df)
print(d)
d.to_csv("crime.csv", index=False)

time.sleep(10)
