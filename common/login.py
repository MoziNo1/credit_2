from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import openpyxl

# 获取信贷加密后的密码，，用于接口测试
login_url = 'http://172.21.1.146:8180/xyjk-erp-app-pc/login?operType=logout'
workbook = openpyxl.open(r'D:\credit\data\146_loginname.xlsx')
worksheet = workbook['Sheet1']
num = 0
for i in range(588):
    chrome_option = Options()
    chrome_option.add_argument('--headless')
    chrome_option.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_option)
    driver.get(login_url)
    driver.maximize_window()
    try:
        time.sleep(3)
        print(worksheet[f'A{i}'].value)
        driver.find_element_by_xpath('//*[@placeholder="请输入您的用户名"]').send_keys(worksheet[f'A{i}'].value)
        driver.find_element_by_xpath('//*[@placeholder="请输入您的密码"]').send_keys('1')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[7]/button').click()
        time.sleep(2)
        num += 1
        print(f'已获取{num}个')
    except Exception as e:
        print('继续干')
    finally:
        driver.close()



