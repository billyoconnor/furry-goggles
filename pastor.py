#Function for uploading value
from selenium import webdriver

driver = webdriver.Firefox()

def pastorID(driver, ID, sheetCell):
    driver = driver.find_element_by_id(ID)
    driver.clear()
    driver.send_keys(sheetCell)

def pastorXPath(xpath, sheetCell):
    driver = webdriver.Firefox()
    driver = driver.find_element_by_xpath(xpath)
    driver.clear()
    driver.send_keys(sheetCell)

