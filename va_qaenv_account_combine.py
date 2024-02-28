from selenium import webdriver
import pyautogui
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


PATH =(r"C:\Users\samuel.lee\Desktop\chromedriver.exe")
driver = webdriver.Chrome(PATH)

driver.get('https://qa.infocast-v3.com:30080/login')
driver.maximize_window()
wait=WebDriverWait(driver, 5)
element=wait.until(EC.presence_of_element_located((By.ID, "tenant")))
driver.find_element_by_id("tenant").send_keys('pleaseentertenant')
driver.find_element_by_id("uname").send_keys('pleaseenteruname')
driver.find_element_by_id("pass").send_keys('pleaseenterpass')
driver.find_element_by_class_name("ant-btn.ant-btn-primary.ant-btn-block").click()
driver.implicitly_wait(10) # new add
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/div[2]/button').click()

driver.find_element_by_xpath('//*[@id="AppMenu"]/li[2]/div/span[2]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="AppMenu-account-menu-popup"]/li[2]/span/a').click()
time.sleep(5)
#driver.find_element_by_xpath('//*[@id="rc_select_14"]').send_keys('1000007'+Keys.ENTER)
#driver.find_element(By.XPATH, '//*[@id="rc_select_15"]').send_keys('1000007'+Keys.ENTER)
#dee=driver.find_element(By.CLASS_NAME,  'ant-select-selection-search-input').send_keys('1000007'+Keys.ENTER)  # class method to extract
ve=driver.find_element(By.CSS_SELECTOR, '#rc_select_15').send_keys('1000007'+Keys.ENTER)    # css method to extract   ##rc_select_15
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '#rc_select_9').send_keys('CP001'+Keys.ENTER)  


#Account trade type
ATT=['/html/body/div[4]/div/div/div[2]/div/div/div/div[2]/div']  #/html/body/div[6]/div/div/div[2]/div/div/div/div[2]/div
for att in ATT:
    driver.find_element(By.CSS_SELECTOR, '#rc_select_11').click()
    time.sleep(3)
    x=2
    driver.find_element(By.XPATH, f'/html/body/div[5]/div/div/div[2]/div/div/div/div[{x}]/div').click()
    if x<8:
        x=x+1
        driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[1]/div/div[7]/div/div/div[2]/div[1]/div/div/div/span[2]').click() 
        time.sleep(3)
        driver.find_element(By.XPATH, f'/html/body/div[5]/div/div/div[2]/div/div/div/div[{x}]/div').click()   #TT002
        time.sleep(5)
        if x==3:
            x=x+1
        driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[1]/div/div[7]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
        driver.find_element(By.XPATH, f'/html/body/div[5]/div/div/div[2]/div/div/div/div[{x}]/div').click()
        time.sleep(5)
        if x==4:
            x=x+1
            driver.find_element(By.XPATH,'//*[@id="dynamic_rule"]/div/div[1]/div/div[7]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, f'/html/body/div[5]/div/div/div[2]/div/div/div/div[{x}]/div').click()
        time.sleep(5)    
        if x==5:
            x=x+1
            driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[1]/div/div[7]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
            driver.find_element(By.XPATH, f'/html/body/div[5]/div/div/div[2]/div/div/div/div[{x}]/div').click()
            break

# Account status loop
def asl():
    i=1
    while True:
            i=i+1
            driver.find_element(By.XPATH, '//*[@id="rc_select_7"]').click()  #blank dropdown
            time.sleep(3)
            driver.find_element(By.XPATH, f'/html/body/div[6]/div/div/div[2]/div/div/div/div[{i}]/div').click()   #[5] -> [6]
            driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[1]/div/div[10]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
            time.sleep(3)
            i=i+1
            driver.find_element(By.XPATH, f'/html/body/div[6]/div/div/div[2]/div/div/div/div[{i}]/div').click()
            driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[1]/div/div[10]/div/div/div[2]/div[1]/div/div/div/span[2]').click()  #dropdown 
            time.sleep(3)
            i=i+1
            driver.find_element(By.XPATH, f'/html/body/div[6]/div/div/div[2]/div/div/div/div[{i}]/div').click()
            driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[1]/div/div[10]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
            time.sleep(3)
            i=i+1
            driver.find_element(By.XPATH, f'/html/body/div[6]/div/div/div[2]/div/div/div/div[{i}]/div').click()
            break
asl()
        


time.sleep(2)
driver.find_element(By.XPATH, "//form[@id='dynamic_rule']/div/div[2]/button").click()   #reset btn

driver.find_element(By.CSS_SELECTOR, '#rc_select_9').send_keys('CP002'+Keys.ENTER)  
#driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div/div/div/span[2]').click() 

asl() 


time.sleep(2)
driver.close()

#EID =  
#driver.find_element_by_xpath('//*[@id="rc_select_72"]').send_keys('HKG'+Keys.ENTER)
#ACcountry = 


#driver.find_element(By.CLASS_NAME, "ant-select-selection-item").send_keys('HKG')




'''from selenium.webdriver.common.action_chains import ActionChains

value = “Test”

actions = ActionChains(driver)

actions.send_keys(value)

actions.perform()'''

# for i in range(2, 4):
#     time.sleep(5)
#     driver.find_element_by_xpath('//*[@id="rc_select_1"]').click()
#     xpath=f"/html/body/div[3]/div/div/div[2]/div/div/div/div[{i}]/div"
#     #driver.find_element_by_xpath('//*[@id="dynamic_rule"]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
#     driver.find_element_by_xpath(xpath).click()
   

#can del    
# i = 1
# while True:
#     # i = 3
#     i +=1
#     driver.find_element_by_xpath('//*[@id="rc_select_1"]').click()
#     time.sleep(3)
#     driver.find_element_by_xpath(f'/html/body/div[3]/div/div/div[2]/div/div/div/div[{i}]/div').click()
#     time.sleep(3)
#     driver.find_element_by_xpath('//*[@id="dynamic_rule"]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
#     driver.find_element_by_xpath(f'/html/body/div[3]/div/div/div[2]/div/div/div/div[{i}]/div').click()
#/can del

# pi=["True","False"]
# i=0
# for i in pi :
#     print (i)

'''
pi=['/html/body/div[3]/div/div/div[2]/div/div/div/div[2]/div']    #field value is true

for b in pi:
    driver.find_element_by_xpath('//*[@id="rc_select_1"]').click()
    time.sleep(3)
    i = 2
    
    driver.find_element_by_xpath(f'/html/body/div[3]/div/div/div[2]/div/div/div/div[{i}]/div').click()
    if i == 2 :
        i=i+1
        driver.find_element_by_xpath('//*[@id="dynamic_rule"]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
        time.sleep(3)
        driver.find_element_by_xpath(f'/html/body/div[3]/div/div/div[2]/div/div/div/div[{i}]/div').click()



et=['/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div']
for c in et:
     driver.find_element_by_xpath('//*[@id="rc_select_0"]').click()
     time.sleep(3)
     ii=2

     driver.find_element_by_xpath(f'/html/body/div[4]/div/div/div[2]/div/div/div/div[{ii}]/div').click()
     if ii<6:
         ii=ii+1
     driver.find_element_by_xpath('//*[@id="dynamic_rule"]/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
     time.sleep(3)
     driver.find_element_by_xpath(f'/html/body/div[4]/div/div/div[2]/div/div/div/div[{ii}]/div').click()


eit=['/html/body/div[6]/div/div/div[2]/div/div/div/div[2]/div']
for d in eit:
    driver.find_element_by_xpath('//*[@id="rc_select_3"]').click()
    time.sleep(3)
    iii=2
    driver.find_element_by_xpath(f'/html/body/div[5]/div/div/div[2]/div/div/div/div[{iii}]/div').click()
    if iii<9:
        iii=iii+1
    driver.find_element_by_xpath('//*[@id="dynamic_rule"]/div/div[1]/div/div[8]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
    time.sleep(3)
    driver.find_element_by_xpath(f'/html/body/div[5]/div/div/div[2]/div/div/div/div[{iii}]').click()
    time.sleep(3)
    if iii == 3:
        iii=iii+1
    driver.find_element_by_xpath('//*[@id="dynamic_rule"]/div/div[1]/div/div[8]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
    driver.find_element_by_xpath(f'/html/body/div[5]/div/div/div[2]/div/div/div/div[{iii}]').click()   # 3-passport
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="dynamic_rule"]/div/div[1]/div/div[8]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
    if iii==4:
        iii=iii+1
    driver.find_element_by_xpath(f'/html/body/div[5]/div/div/div[2]/div/div/div/div[{iii}]').click() #legal entity identifier
    time.sleep(3)
    if iii==5:   #new add
        iii=iii+1
    driver.find_element_by_xpath('//*[@id="dynamic_rule"]/div/div[1]/div/div[8]/div/div/div[2]/div[1]/div/div/div/span[2]').click()    
    driver.find_element_by_xpath(f'/html/body/div[5]/div/div/div[2]/div/div/div/div[{iii}]').click()  #BR cert
    time.sleep(2)
    if iii==6:
        iii=iii+1
    driver.find_element_by_xpath('//*[@id="dynamic_rule"]/div/div[1]/div/div[8]/div/div/div[2]/div[1]/div/div/div/span[2]').click() 
    driver.find_element_by_xpath(f'/html/body/div[5]/div/div/div[2]/div/div/div/div[{iii}]').click()
    if iii==7:
        iii=iii+1
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="dynamic_rule"]/div/div[1]/div/div[8]/div/div/div[2]/div[1]/div/div/div/span[2]').click() 
    driver.find_element_by_xpath(f'/html/body/div[5]/div/div/div[2]/div/div/div/div[{iii}]').click()
'''
    
    # if iii ==5 :
    #     iii=iii+1
    #     driver.find_element_by_xpath('//*[@id="dynamic_rule"]/div/div[1]/div/div[8]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
    #     time.sleep(3)
    #     driver.find_element_by_xpath(f'/html/body/div[5]/div/div/div[2]/div/div/div/div[{iii}]').click()
   






# /html/body/div[1]/div/div[2]/main/div/main/form/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div/div/span[1]/input
# /html/body/div[4]/div/div/div[2]/div/div/div/div[2]/div
# /html/body/div[4]/div/div/div[2]/div/div/div/div[3]/div"# Work_backup" 
