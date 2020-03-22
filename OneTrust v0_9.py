#Spreadsheet uploader for GDPR checklist into Onetrust
import os
import tkinter.messagebox
from tkinter import Tk
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import dataTran as dt
import pastor
import time

# Begin web work
    #Begin login section
driver = webdriver.Firefox()
driver.get("https://app-eu.onetrust.com/auth/login") #open login page
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
tkinter.messagebox.showinfo(title="Wait!", message="Please Allow page to load in background before clicking 'Ok'")

email_form = pastor.pastorID(driver,'ot_form-element_0',dt.ws3['F6'].value,'enter')

tkinter.messagebox.showinfo(title="Wait!", message="Please Allow page to load in background before clicking 'Ok'")

password_form = pastor.pastorID(driver,'ot_form-element_1','Letmein1!','enter')


tkinter.messagebox.showinfo(title="Wait!", message="Please Allow page to load in background before clicking 'Ok'")
#End Login section

#Begin Assessment Details Section
#Put an Option here to edit an existing assesment

driver.get("https://app-eu.onetrust.com/app/#/pia/assessment/wizard/info/1e3ef905-4efd-4b74-835a-c0bc9767e65d/1")
tkinter.messagebox.showinfo(title="Wait!", message="Please Allow page to load in background before clicking 'Ok'")
nameID = driver.find_element(By.XPATH, '//input[@placeholder="Enter Assessment Name"]').get_attribute("ID")
name = driver.find_element_by_id(nameID)
name.send_keys(dt.assName)

approver = driver.find_element(By.XPATH, '//div[5]/div/ot-org-user-multi-select/div/div/div/ot-org-user/div/div/ot-lookup/div/div/div/input[@placeholder="Select an Assignee"]')
approver.click()
approver.clear
approver.send_keys('James Taylor')
#i = 0
#while i < 4:
#	respondent.send_keys(Keys.ARROW_DOWN)
#	i = i + 1

time.sleep(2)

clickName = driver.find_element_by_xpath("//*[contains(@style,'translateY(0px)')]")
clickName.click()

respondent = driver.find_element(By.XPATH, '//div[6]/div/ot-org-user-multi-select/div/div/div/ot-org-user/div/div/ot-lookup/div/div/div/input[@placeholder="Select an Assignee"]')
respondent.click()
respondent.clear()
time.sleep(2)
respondentName = driver.find_element_by_xpath("//div[6]/div/ot-org-user-multi-select/div/div/div/ot-org-user/div/div/ot-lookup/div/div/div[2]/ul/od-virtualscroll/div/od-virtualrow[1][contains(@style,'translateY(0px)')]")
respondentName.click()


#tkinter.messagebox.showinfo(title="Hold up!", message="Please Complete the Approver and Respondent fields BEFORE clicking 'ok'")
launchButton = driver.find_element(By.XPATH, '//button[@ot-auto-id="AAStartWizardLaunchButton"]')
launchButton.click()

tkinter.messagebox.showinfo(title="Hold up!", message="Please wait until page completes loading before clicking 'ok'")


#Post Launch
projectDetails = pastor.pastorXPath(driver, '//aa-section-list-filter/section/section/div[3]/div[2]', 0, 0, 1)

wb4 = openpyxl.load_workbook('dataframe.xlsx')
ws4 = wb4['Sheet1']
# Start filling in details from data sheet
tkinter.messagebox.showinfo(title="Hold up!", message="Please wait until page completes loading before clicking 'ok'")
requestorName = pastor.pastorXPath(driver, '//aa-rich-text-editor/div/div/ot-rich-text-editor/div[2]/div[1]', ws4['f5'].value, 0, 0)

contactDetails = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[2]/div/div/div/div[1]/aa-rich-text-editor/div/div/ot-rich-text-editor/div[2]/div[1]')
contactAnswer = ws4['f6'].value
contactDetails.send_keys(contactAnswer)
privacyChampion = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[3]/div/div/div/div/div[1]/button')
privacyChampion.click()
localMarket = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[4]/div/div/div/div[1]/aa-multichoice-dropdown/div/div/ot-lookup/div/div/div[1]/input')
localMarket.click()
vfGroup = driver.find_element_by_xpath('//*[@id="listbox-option-unique-id-[object Object]"]')
vfGroup.click() #vfGroup is a hard coded variable!!
businessOwner = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[6]/div/div/div/div[1]/aa-rich-text-editor/div/div/ot-rich-text-editor/div[2]/div[1]')
businessAnswer = ws4['f10'].value
businessOwner.send_keys(businessAnswer)
produceProcess = ws4['f11'].value #Product or process value
if produceProcess == 'Product' :
	product = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[7]/div/div/div/aa-multichoice-buttons/div/div/div[1]/button')
	product.click()
elif produceProcess == 'Process':
	product = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[7]/div/div/div/aa-multichoice-buttons/div/div/div[2]/button')
	product.click()
else :
    pass
explainProduct = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[7]/div/div/div/div/aa-rich-text-editor/div/div/ot-rich-text-editor/div[2]/div[1]')
explainProductAss = ws4['f12'].value
explainProduct.send_keys(explainProductAss)
describeProject = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[9]/div/div/div/div[1]/aa-rich-text-editor/div/div/ot-rich-text-editor/div[2]/div[1]')
describeProjectAss = ws4['f15'].value
describeProject.send_keys(describeProjectAss)
whoDataAss = ws4['f18'].value
if whoDataAss == 'Consumer customer' or whoDataAss == 'Enterprise customer':
	whoData = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[11]/div/div/div/aa-multichoice-buttons/div/div/div[1]/button')
	whoData.click()
elif whoDataAss == 'Employees':
	whoData = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[11]/div/div/div/aa-multichoice-buttons/div/div/div[2]/button')
	whoData.click()
elif whoDataAss == 'Prospective employees':
	whoData = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[11]/div/div/div/aa-multichoice-buttons/div/div/div[3]/button')
	whoData.click()
elif whoDataAss == 'Contractors':
	whoData = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[11]/div/div/div/aa-multichoice-buttons/div/div/div[4]/button')
	whoData.click()
elif whoDataAss == 'Suppliers':
	whoData = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[11]/div/div/div/aa-multichoice-buttons/div/div/div[5]/button')
	whoData.click()
elif whoDataAss == 'General Public':
	whoData = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[11]/div/div/div/aa-multichoice-buttons/div/div/div[6]/button')
	whoData.click()
elif whoDataAss == 'Not Sure':
	whoData = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[11]/div/div/div/aa-multichoice-buttons/div/div/div[7]/button')
	whoData.click()
else:
	pass

whoExplain = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[11]/div/div/div/div/aa-rich-text-editor/div/div/ot-rich-text-editor/div[2]/div[1]')
whoExplainAss = ws4['f19'].value
whoExplain.send_keys(whoExplainAss)

vunPeopleAss = ws4['f20'].value
if vunPeopleAss == 'Children':
	vunPeople = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[12]/div/div/div/aa-multichoice-buttons/div/div/div[1]/button')
	vunPeople.click()
elif vunPeopleAss == 'Elderly':
	vunPeople = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[12]/div/div/div/aa-multichoice-buttons/div/div/div[2]/button')
	vunPeople.click()
elif vunPeopleAss == 'People with limited mental capacity':
	vunPeople = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[12]/div/div/div/aa-multichoice-buttons/div/div/div[3]/button')
	vunPeople.click()
elif vunPeopleAss == 'Not Sure':
	vunPeople = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[12]/div/div/div/aa-multichoice-buttons/div/div/div[4]/button')
	vunPeople.click()
elif vunPeopleAss == 'NO':
	vunPeople = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/div/div/assessment-detail-question-group/assessment-detail-question[12]/div/div/div/aa-multichoice-buttons/div/div/div[5]/button')
	vunPeople.click()
else:
	pass

saveAndExit = driver.find_element_by_xpath('/html/body/app-root/div/div/ui-view/ui-view/ui-view/div/div/div[1]/ui-view/downgrade-assessment-detail/section/div[2]/div/div[2]/aa-section-footer/footer/div[2]/div[2]/button[1]')
saveAndExit.click()
tkinter.messagebox.showinfo(title="Info", message="Program execution complete")

