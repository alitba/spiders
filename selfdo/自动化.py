##谷歌无头浏览器
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
Chrome_options=Options()
Chrome_options.add_argument("--headless")
Chrome_options.add_argument("--disable-gpu")
option=ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

bro=webdriver.Chrome(executable_path="D:\Chromedriver\chromedriver.exe",options=option)


bro.get("http://www.baidu.com")
time.sleep(2)
bro.save_screenshot("./3.png")