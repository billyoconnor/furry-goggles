#Function for uploading value
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def pastorID(driver, ID, sheetCell, pressEnter=0, clickOnElement=0):
    """Takes the selenium webdriver from main, finds a field by ID, and uploads the specified excel cell value"""
    driver = driver.find_element_by_id(ID)
    driver.clear()
    driver.send_keys(sheetCell)
    if pressEnter:
        driver.send_keys(Keys.RETURN)
    else:
        pass
    if clickOnElement:
        driver.click()
    else:
        pass

def pastorXPath(driver, xpath, sheetCell=0, pressEnter=0, clickOnElement=0):
    """Takes the selenium webdriver from main, finds a field by xpath, and uploads the specified excel cell value"""
    driver = driver.find_element_by_xpath(xpath)
    if sheetCell:
        driver.clear()
        driver.send_keys(sheetCell)
    else:
        pass
    if pressEnter:
        driver.send_keys(Keys.RETURN)
    else:
        pass
    if clickOnElement:
        driver.click()
    else:
        pass

