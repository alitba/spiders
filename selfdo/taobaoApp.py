# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "9889954632564a4d45"
caps["appPackage"] = "com.taobao.taobao"
caps["appActivity"] = "com.taobao.tao.welcome.Welcome"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

undefined = driver.find_elements_by_name("")

driver.quit()
