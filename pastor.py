#Function for uploading value
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from testfunc import sillyFunc

sillyFunc(6,4)
def pastorXPath(xpath, sheetCell):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get('https://www.google.com/')
    driver = driver.find_element_by_xpath(xpath)
    driver.clear()
    driver.send_keys(sheetCell)
    print(sheetCell)

#pastorXPath('/html/body/div/div[4]/form/div[2]/div[1]/div[1]/div/div[2]/input', 'Billy Webb')
#testfunc(4,6)
