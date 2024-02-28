from selenium import webdriver
import pyautogui
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import psycopg2 # new only for check db 

PATH =(r"C:\Users\samuel.lee\Desktop\chromedriver.exe")
driver = webdriver.Chrome(PATH)

driver.implicitly_wait(10)
driver.get('https://dev.infocast-v3.com:30080/login')
driver.maximize_window()
wait=WebDriverWait(driver, 5)
element=wait.until(EC.presence_of_element_located((By.ID, "tenant")))
driver.find_element_by_id("tenant").send_keys('pleaseentertenant')
driver.find_element_by_id("uname").send_keys('pleaseenteruname')
driver.find_element_by_id("pass").send_keys('pleaseenterpass')
driver.find_element_by_class_name("ant-btn.ant-btn-primary.ant-btn-block").click()
#driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(3) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > div > div:nth-child(2) > button').click()   #if use dev env, please # this line

#time.sleep(5)
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="AppMenu"]/li[8]/div/span[2]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="AppMenu-product-popup"]/li[3]/span/a').click()
driver.find_element(By.CSS_SELECTOR, '#root > div > div.ant-layout.ant-layout-has-sider.section-layout > main > div > div > div > div.page-header-heading-extra > div > div:nth-child(2) > button').click()
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div/input').send_keys('GOLD')
driver.find_element(By.XPATH, '//*[@id="rc_select_3"]').send_keys('HKEY-HashKey Group'+Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="rc_select_4"]').send_keys('Token/Fiat-Exchange Digital Assets to Fiat Currency'+Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/input').send_keys('GOLD'+Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/input').send_keys('黃金'+Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/input').send_keys('黃金'+Keys.ENTER)
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/div[2]/button').click()    #create


conn= psycopg2.connect(database="XX", user="postgres", password="XX", host="XXX.XXX.XX.XXX", port="XXXX")
print ("y")
cur = conn.cursor()
cur.execute("select * from v3ibroker.tenant_product_sub_type where product_sub_type ='GOLD';")
rows = cur.fetchall()
for i in rows:
    uj=print (i[4])
    uj='GOLD'
    if uj =="GOLD":
        print ('truetrue')
    else:
        print ('false')
    
conn.close()
print('add-pass')

driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div/input').send_keys('GOLD'+Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[2]/button[2]').click()

driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/main/div/main/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[7]/span/button[3]').click() #edit
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div/div/div[4]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/input').send_keys(Keys.CONTROL, "a")
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div/div/div[4]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/input').send_keys(Keys.DELETE)#send_keys('GL')
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div/div/div[4]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/input').send_keys('GL')
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/input').send_keys(Keys.CONTROL, "a")
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/input').send_keys(Keys.DELETE)#send_keys('黃金1')
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/input').send_keys('黃金1')
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div/div/div[4]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/input').send_keys(Keys.CONTROL, "a")
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div/div/div[4]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/input').send_keys(Keys.DELETE)
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div/div/div[4]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/input').send_keys('黃金1')#send_keys('黃金1')
driver.find_element(By.CSS_SELECTOR, '#generalInformation > footer > div > div:nth-child(2) > button.ant-btn.ant-btn-primary').click()
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/div[2]/button').click()    #mod 

conn= psycopg2.connect(database="XXXX", user="postgres", password="XXXX", host="XXX.XXX.XX.XXX", port="XXXX")
print ("y")
curr = conn.cursor()
curr.execute("select * from v3ibroker.tenant_product_sub_type where product_sub_type_name_en_us ='GL';")
rows = curr.fetchall()
for x in rows:
    print (x[5])
    ee=print (x[5])
    ee='黃金1'
    if ee =="黃金1":
        print ("truetrue")
    else:
        print ('false')
        
conn.close()
print('mod-pass')




driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div/input').send_keys('GOLD'+Keys.ENTER)   #del
driver.find_element(By.XPATH, '//*[@id="dynamic_rule"]/div/div[2]/button[2]').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/main/div/main/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[7]/span/button[4]').click()
driver.implicitly_wait(10)
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(3) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > div > div:nth-child(2) > button').click()
time.sleep(5)
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(3) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > div > div:nth-child(2) > button').click()

print('finish')



   
   "# Work_backup" 
