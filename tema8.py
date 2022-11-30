from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome() # Seteaza driverul
import time
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
print(driver.title) # printeaza titlu paginei
first_name = driver.find_element(By.NAME, 'firstname')
first_name.send_keys('Deleanu')
last_name = driver.find_element(By.NAME, 'lastname')
last_name.send_keys('Costi')
driver.find_element(By.ID, 'sex-0').click()
driver.find_element(By.ID, 'exp-0').click()
date = driver.find_element(By.ID, 'datepicker')
date.send_keys('23.11.2021')
driver.find_element(By.ID, 'profession-1').click()
driver.find_element(By.ID, 'tool-2').click()
time.sleep(2)

driver.quit() # inchide pagina

#------------ Link text

driver.get('https://formy-project.herokuapp.com/') # Navigam catre un url
driver.find_element(By.LINK_TEXT, 'Checkbox').click()
driver.find_element(By.ID, 'checkbox-1').click()
time.sleep(2)

#-----------

driver.get('https://formy-project.herokuapp.com/') # Navigam catre un url
driver.find_element(By.LINK_TEXT, 'Datepicker').click()
driver.find_element(By.ID, 'datepicker').click()
time.sleep(2)

#-----------

driver.get('https://formy-project.herokuapp.com/') # Navigam catre un url
driver.find_element(By.LINK_TEXT, 'Switch Window').click()
driver.find_element(By.ID, 'alert-button').click()
time.sleep(2)

#-----------   Parțial link text

driver.get('https://formy-project.herokuapp.com/')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Radio').click()
driver.find_element(By.ID, 'radio-button-1').click()
time.sleep(2)
#-----------

driver.get('https://formy-project.herokuapp.com/')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Page ').click()
driver.find_element(By.ID, 'name').send_keys('Deleanu Constantin')
driver.find_element(By.ID, 'date').send_keys('11.29.2022')
time.sleep(2)

#-----------

driver.get('https://formy-project.herokuapp.com/')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Key').click()
driver.find_element(By.ID, 'name').send_keys('Deleanu Costi')
driver.find_element(By.ID, 'button').click()
time.sleep(2)

#-------- Name

driver.get('http://www.seleniumframework.com/Practiceform/')
driver.find_element(By.NAME, 'name').send_keys('Costi')
driver.find_element(By.NAME, 'email').send_keys('costidelean@gmail.com') # completeaza adresa de mail de la subscribe in loc de contact us
driver.find_element(By.NAME, 'telephone').send_keys('0749706619')
driver.find_element(By.NAME, 'country').send_keys('Romania')
driver.find_element(By.NAME, 'company').send_keys('Amazon')
driver.find_element(By.NAME, 'message').send_keys('Daca vedeti acest mesaj, codul functioneaza.')
time.sleep(2)

#------------ by Tag

# Navigam catre alta pagina
driver.get('https://formy-project.herokuapp.com/form')
driver.find_element(By.TAG_NAME, 'input').send_keys('Costi')# Selector by Tag - ia primul tot timpul - se poate folosi doar daca avem element unic
input_list = driver.find_elements(By.TAG_NAME, 'input') # Gasim mai multe si le punem in lista
input_list[1].send_keys('Deleanu')
input_list[2].send_keys('Automation QA')
driver.find_element(By.ID, 'radio-button-3').click()
driver.find_element(By.ID, 'checkbox-1').click()
time.sleep(2)

#---------------

driver.get('https://www.techlistic.com/p/selenium-practice-form.html') # Navigam catre un url
driver.find_element(By.TAG_NAME, 'input').send_keys('Costi')
input_list = driver.find_elements(By.TAG_NAME, 'input')
input_list[1].send_keys('Deleanu')
driver.find_element(By.ID, 'sex-0').click()
driver.find_element(By.ID, 'exp-0').click()
driver.find_element(By.ID, 'datepicker').send_keys('30.11.2022')
driver.find_element(By.ID, 'profession-1').click()
driver.find_element(By.ID, 'tool-2').click()
time.sleep(2)

#------------- By class name

driver.get('https://formy-project.herokuapp.com/form')
driver.find_element(By.CLASS_NAME, 'form-control').send_keys('Costi')
driver.find_elements(By.CLASS_NAME, 'form-control')[1].send_keys('Deleanu')
driver.find_elements(By.CLASS_NAME, 'form-control')[2].send_keys('Automation QA')
driver.find_element(By.ID, 'radio-button-3').click()
driver.find_element(By.ID, 'checkbox-1').click()
time.sleep(2)

#-------------- CSS

driver.get('http://www.seleniumframework.com/Practiceform/')
driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Name *"]').send_keys('Costi')
driver.find_element(By.CSS_SELECTOR, 'input[placeholder="E-mail *"]').send_keys('costidelean@gmail.com')
driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Telephone *"]').send_keys('0749704619')
time.sleep(3)
