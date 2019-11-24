from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
bro = webdriver.Chrome(executable_path="D:\Chromedriver\chromedriver.exe")

wait=WebDriverWait(bro,60)

def get_first_page():
    try:

        url = "https://www.amazon.cn/b?node=1841388071&tag=baiduiclickcn-23&ref=AGS_1738_zhj_45437"
        bro.get(url)
        # page_text=bro.page_source
        # print(page_text)
        input_ele=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#twotabsearchtextbox")))
        submit = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#nav-search > form > div.nav-right > div > input")))
        # input_ele.clear()
        input_ele.send_keys("电脑")
        submit.click()
        total=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#J_bottomPage > span.p-skip > em:nth-child(1) > b")))
        return total.text
        # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '')))
    except TimeoutException:
        print("超时取消")

def main():
    total=get_first_page()
    print(total)

if __name__ == '__main__':
    main()







# print(page_text)

# wait=WebDriverWait(bro,10)
# keyword=input("请输入关键字：")
# def index_page():
#     try:
#         url="https://search.jd.com/Search?keyword="+keyword
#
#
#         submit=wait.until(
#             EC.presence_of_element_located((By.CSS_SELECTOR,"#search-2014 > div > button > i")))
#         input_ele.clear()
#         input_ele.send_keys("电脑")
#         submit.click()
#
#     except TimeoutException:
#         index_page()







