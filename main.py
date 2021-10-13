
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
#from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
#options.headless = True 
options.add_argument('--no-proxy-server')
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
chromedriver_autoinstaller.install(cwd=True)
driver = webdriver.Chrome(options=options)


from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import TimeoutException
import time

resp = driver.get('https://meine.postbank.de/#/login')

os.chdir(os.path.normpath(os.getcwd() + os.sep + os.pardir)) # we  go back in path one step to accses user.txt

f= open('user.txt', "r")
userName= f.read()
f.close()

inputUsername =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'postbankId')))
inputUsername.send_keys(userName)


element = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div[1]/div/form/div[2]/button')))
element.click()  # after click we recive in the bank app 'BestSign' on our phone a code for 2 factor authentification

twoFactorAuthentificationWait = WebDriverWait(driver, 130).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='c-table-list__body']"))) 
amountsTable = driver.find_elements_by_class_name("c-table-list__body")


accountsList=[]
for account in amountsTable:
    accountsList.append(account.text)
accountsList= accountsList[0].split('\n')  

giroKontoBalance=accountsList[3]
visaBalance=accountsList[10]
print('Girokonto balance is ',giroKontoBalance)
print('Visa balance is ',visaBalance)