from selenium import webdriver
import pyautogui
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


PATH =(r"C:\Users\samuel.lee\Desktop\chromedriver.exe")
driver = webdriver.Chrome(PATH)

driver.get('https://dev.infocast-v3.com:30080/login')
driver.maximize_window()
wait=WebDriverWait(driver, 5)
element=wait.until(EC.presence_of_element_located((By.ID, "tenant")))
driver.find_element_by_id("tenant").send_keys('pleaseentertenant')
driver.find_element_by_id("uname").send_keys('pleaseenteruname')
driver.find_element_by_id("pass").send_keys('pleaseenterpass')
driver.find_element_by_class_name("ant-btn.ant-btn-primary.ant-btn-block").click()

time.sleep(5)
driver.implicitly_wait(10)
#driver.find_element(By.CSS_SELECTOR, '#AppMenu > li:nth-child(11) > div > span.ant-menu-title-content').click()   ##AppMenu > li:nth-child(11) > div > span.ant-menu-title-content  ;//*[@id="AppMenu"]/li[11]/div/span[2]
driver.find_element(By.XPATH, '//*[@id="AppMenu"]/li[11]/div/span[2]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="AppMenu-charge-menu-popup"]/li[2]/span/a').click()


driver.find_element(By.CSS_SELECTOR, '#rc_select_0').click()
for i in range (2, 4):
    driver.find_element(By.XPATH, f'/html/body/div[3]/div/div/div[2]/div/div/div/div[{i}]/div').click()
    
    
    for j in range (2, 4):
        driver.find_element(By.CSS_SELECTOR, '#rc_select_1').click()
        driver.find_element(By.XPATH, f'/html/body/div[4]/div/div/div[2]/div/div/div/div[{j}]/div').click()
        j+=1
        driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
        driver.find_element(By.XPATH, f'/html/body/div[4]/div/div/div[2]/div/div/div/div[{j}]/div').click()
        i=i+1
        driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
        driver.find_element(By.XPATH, f'/html/body/div[3]/div/div/div[2]/div/div/div/div[{i}]/div').click()
    i=i+1
    driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
    
    driver.find_element(By.XPATH, f'/html/body/div[3]/div/div/div[2]/div/div/div/div[3]/div').click()
'''below is old my code
x=['/html/body/div[4]/div/div/div[2]/div/div/div/div[2]/div']
y=['/html/body/div[4]/div/div/div[2]/div/div/div/div[2]/div']
for i in x:
    driver.find_element(By.XPATH, '//*[@id="rc_select_0"]').click()
    time.sleep(3)
    xx=2
    yy=2
    driver.find_element(By.XPATH, f'/html/body/div[3]/div/div/div[2]/div/div/div/div[{xx}]/div').click()   #exchang id 0
    driver.find_element(By.XPATH, '//*[@id="rc_select_1"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, f'/html/body/div[4]/div/div/div[2]/div/div/div/div[{yy}]/div').click()   #gst 0
    driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
    driver.implicitly_wait(5)
    yy=yy+1
    driver.find_element(By.XPATH, f'/html/body/div[4]/div/div/div[2]/div/div/div/div[{yy}]/div').click()   #gst 1
    driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
    xx=xx+1
    driver.find_element(By.XPATH, f'/html/body/div[3]/div/div/div[2]/div/div/div/div[{xx}]/div').click()  #exchang id 1
    driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div/div/span[2]').click()   #gst field
    driver.find_element(By.XPATH, f'/html/body/div[4]/div/div/div[2]/div/div/div/div[{yy}]/div').click()     # click gst 1 to avoid the element click intercepted 
    yy=yy-1
    driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
    driver.find_element(By.XPATH, f'/html/body/div[4]/div/div/div[2]/div/div/div/div[{yy}]/div').click()

    # driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
    # time.sleep(3)
    # xx=xx+1
    # driver.find_element(By.XPATH, f'/html/body/div[3]/div/div/div[2]/div/div/div/div[{xx}]/div').click()
'''
'''
    for j in y:
        driver.find_element(By.XPATH, '//*[@id="rc_select_1"]').click()
        time.sleep(3)
        yy=2
        driver.find_element(By.XPATH, f'/html/body/div[4]/div/div/div[2]/div/div/div/div[{yy}]/div').click()
        driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div/div/span[2]').click()
        time.sleep(3)
        yy=yy+1
        driver.find_element(By.XPATH, f'/html/body/div[4]/div/div/div[2]/div/div/div/div[{yy}]/div').click()
        break
    '''   

"# Work_backup"   
