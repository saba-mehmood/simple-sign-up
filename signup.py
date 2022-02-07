
import email
from threading import Thread
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import re
from config import TestData
#from yopmail import Yopmail


      
    
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://avaxdev.akru.co/")
window_before = driver.window_handles[0]
driver.find_element(By.CLASS_NAME,'primary-btn').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[4]/div[1]/form/div/label[1]/span[1]/span[1]/input').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[4]/div[1]/form/button').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/section/div/div/div[1]/button').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/section/div/div/div[1]/button').click()
driver.find_element(By.NAME,'firstName').send_keys(TestData.FIRST_NAME)
driver.find_element(By.NAME,'lastName').send_keys(TestData.LAST_NAME)
driver.find_element(By.NAME,'email').send_keys(TestData.EMAIL)
driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[1]/fieldset/div/label[1]/span[2]').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[1]/div[4]/label/span[1]/span[1]/input').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[2]/button').click()
time.sleep(10)


"""HANDLING ALERT IF EMAIL IS ALREADY REGISTERED"""

try:
  #switch to alert and print pop up text
    element_alert = driver.find_element(By.CLASS_NAME, 'Toastify__toast-body').get_attribute("textContent")
    time.sleep(3)
    print(element_alert)    
    driver.quit()   
except NoSuchElementException:
   
  print("exception handled")
   


#Yopmail(TestData.EMAIL)

"""YOPMAIL"""
driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://yopmail.com/en/")
time.sleep(20)
mail_field = driver.find_element(By.CLASS_NAME,'ycptinput')
mail_field.send_keys(Keys.CONTROL, "a")
mail_field.send_keys(Keys.BACKSPACE)
mail_field.send_keys(TestData.EMAIL)
driver.find_element(By.XPATH,'//*[@id="refreshbut"]/button/i').click()
frame_login = driver.switch_to.frame(driver.find_element(By.ID,'ifmail'))
try:
         login_btn= driver.find_element(By.XPATH,'//*[@id="mail"]/div/table/tbody/tr/td/div[2]/div/div/div/div/div/div[4]')
         login_link=driver.find_element(By.LINK_TEXT,'Click here')
         signup_link= driver.find_element(By.LINK_TEXT,'Verify Email')
         if login_btn.is_displayed() and login_btn.is_enabled():
            login_btn.click()  

         elif login_link.is_displayed():
               login_link.click()

         elif signup_link.is_displayed():
               signup_link.click()      
         
         else:
               print("Login Handle")

except:
         continue_signup = driver.find_element(By.XPATH,'/html/body/main/div/div/div/div/div/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/a/b')
      
         if continue_signup.is_displayed():
                continue_signup.click()      
         
         else:
               print("No Login link Found")
driver.close()


""" CONTACT INFO"""

contact_window=driver.switch_to.window(driver.window_handles[1])
# driver.execute_script("window.open()")
time.sleep(10)
#(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[1]/div[1]/div/div/div/input'))).send_keys(TestData.ADDRESS)
driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[1]/div[1]/div/div/div/input').send_keys(TestData.ADDRESS)
select=Select(driver.find_element(By.NAME,'citizenshipLabel'))
select.select_by_visible_text('United States')
select=Select(driver.find_element(By.NAME,'stateName'))
select.select_by_visible_text('Alabama')
driver.find_element(By.NAME,'city').send_keys(TestData.CITY)
driver.find_element(By.NAME,'zipCode').send_keys(TestData.ZIP_CODE)
driver.find_element(By.NAME,'number').send_keys(TestData.PHONE_NO)
driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[1]/div[6]/div/div/div[2]/button').click()
time.sleep(20)

""" OTP"""

driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[2])
driver.get(TestData.OTP)

otp_value= driver.find_element(By.XPATH,'/html/body/pre')

"""USING REGULAR EXPRESSION TO REMOVING TEXT FROM SENTENCE AND GETTING ONLY NUMBERS"""
value = int(re.sub(r"[^\d.]", "", otp_value.text))

"""GETTING LAST 4 NUMBERS FROM WHOLE SENTENCE"""
code=int(str(value)[-4:])
print("value: %s" % code)
driver.close()

"""SWICHING BACK TO CONTACT INFO AND ENTER OTP NUMBER"""
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.NAME,'otp').send_keys(code)

"""DATE PICKER"""
 
datee = driver.find_element(By.XPATH," //input[contains(@value,'08/18/2004')]")
datee.click()
datee.send_keys(Keys.CONTROL, "a")   
datee.send_keys("08/18/2002")  
time.sleep(20)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")      
driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[1]/div[10]/div[2]/input').send_keys(TestData.SSN)
print("error")
driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[2]/div/div/div/button').click()
time.sleep(20)

"""SKIP STEP"""
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#WebDriverWait(driver,10).until(EC.presence_of_element_located(By.XPATH,'/html/body/div[1]/div/section/div/div/div/div/div/div[3]/form/div[2]/div[2]/div/div/button')).click()
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/div/div/div/div/div[3]/form/div[2]/div[2]/div/div/button').click()
time.sleep(4)

"""VERIFY STEP"""
driver.find_element(By.NAME,'point1').click()
driver.find_element(By.NAME,'point2').click()
driver.find_element(By.NAME,'point3').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[2]/div[2]/div/div/button').click()
time.sleep(4)

"""CONNECT WALLET STEP"""
driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[3]/div[2]/div/div/button').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[3]/div[2]/div/div/button').click()
driver.find_element(By.CLASS_NAME,'donwload-btn').click()
time.sleep(2)

"""YOPMAIL"""
driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[2])
driver.get("https://yopmail.com/en/")
mail_field = driver.find_element(By.CLASS_NAME,'ycptinput')
mail_field.send_keys(Keys.CONTROL, "a")
mail_field.send_keys(Keys.BACKSPACE)
mail_field.send_keys(TestData.EMAIL)
driver.find_element(By.XPATH,'//*[@id="refreshbut"]/button/i').click()
frame_login = driver.switch_to.frame(driver.find_element(By.ID,'ifmail'))
try:
         login_btn= driver.find_element(By.XPATH,'//*[@id="mail"]/div/table/tbody/tr/td/div[2]/div/div/div/div/div/div[4]')
         login_link=driver.find_element(By.LINK_TEXT,'Click here')
         if login_btn.is_displayed() and login_btn.is_enabled():
            login_btn.click()

         elif login_link.is_displayed():
               login_link.click()
         
         else:
               print("Login Handle")

except:

         signup_link= driver.find_element(By.LINK_TEXT,'Verify Email')
         if signup_link.is_displayed():
               signup_link.click()
               print(driver.title)
         
         else:
               print("No Login link Found")
time.sleep(4)

driver.switch_to.window(driver.window_handles[1])
time.sleep(40) 
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div[3]/button').click()

try:
  #switch to alert and print pop up text
 element = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast-body'))).get_attribute("textContent")
 print (element)
except NoAlertPresentException:
  print("exception handled")

print("Rest of the programm")


