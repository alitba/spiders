import os
import pickle
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
options=Options()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
brower = webdriver.Chrome(executable_path="D:\Chromedriver\chromedriver.exe",options=options)
wait = WebDriverWait(brower, 60)
from selenium.webdriver.support import expected_conditions as EC


def getTaobaoCookies():
    # get login taobao cookies
    url = "https://www.taobao.com/"
    brower.get("https://login.taobao.com/member/login.jhtml")
    while True:
        print("Please login in taobao.com!")
        time.sleep(3)
        # if login in successfully, url  jump to www.taobao.com
        while brower.current_url ==  url:
            tbCookies  = brower.get_cookies()
            brower.quit()
            cookies = {}
            for item in tbCookies:
                cookies[item['name']] = item['value']
            outputPath = open('taobaoCookies.pickle','wb')
            pickle.dump(cookies,outputPath)
            outputPath.close()
            return cookies


def readTaobaoCookies():
    # if hava cookies file ,use it
    # if not , getTaobaoCookies()
    if os.path.exists('taobaoCookies.pickle'):
        readPath = open('taobaoCookies.pickle', 'rb')
        tbCookies = pickle.load(readPath)
    else:
        tbCookies = getTaobaoCookies()
    return tbCookies

from selenium.webdriver.support.wait import WebDriverWait
tbCookies = readTaobaoCookies()
# wait=WebDriverWait(brower,60)
options=Options()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
brower.get("https://www.taobao.com")


for cookie in tbCookies:
    brower.add_cookie({
        "domain":".taobao.com",
        "name":cookie,
        "value":tbCookies[cookie],
        "path":'/',
        "expires":None
    })
brower.get("https://www.taobao.com")
car=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#mc-menu-hd")))
car.click()

sele=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_SelectAll1")))
sele.click()
time.sleep(0.5)
ensure=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_Go")))
ensure.click()

pay=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#submitOrderPC_1 > div.wrapper > a.go-btn")))
pay.click()

passwd1=brower.find_element_by_css_selector("#payPassword_container > div > i:nth-child(1)")
passwd1.click()
passwd1.send_keys("1")

passwd2=brower.find_element_by_css_selector("#payPassword_container > div > i:nth-child(2)")
passwd2.click()
passwd2.send_keys("0")


passwd3=brower.find_element_by_css_selector("#payPassword_container > div > i:nth-child(3)")
passwd3.click()
passwd3.send_keys("7")


passwd4=brower.find_element_by_css_selector("#payPassword_container > div > i:nth-child(4)")
passwd4.click()

passwd4.send_keys("8")

passwd5=brower.find_element_by_css_selector("#payPassword_container > div > i:nth-child(5)")
passwd5.click()
passwd5.send_keys("3")


passwd6=brower.find_element_by_css_selector("#payPassword_container > div > i:nth-child(6)")
passwd6.click()
passwd6.send_keys("8")









