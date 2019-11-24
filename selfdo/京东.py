from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
from urllib.parse import quote
##J_bottomPage > span.p-num > a.curr

options=ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])

bro = webdriver.Chrome(executable_path="D:\Chromedriver\chromedriver.exe",options=options)
wait=WebDriverWait(bro,60)
KEYWOR="电脑"

def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第',page , '页')

    url = "http://www.jd.com"

    bro.get(url=url)
    get_products()

    time.sleep(6)
    input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#key')))
    input.clear()
    input.send_keys(KEYWOR)

    submit = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#search > div > div.form > button')))
    submit.click()
    get_products()
    time.sleep(6)
    next_page()
    # submit = wait.until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.pn-next')))
    #
    # submit.click()

#
def next_page():


        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.pn-next')))

        submit.click()

        get_products()




        # else:
        #     index_page(page)



        ##J_bottomPage > span.p-num > a.curr
#J_bottomPage > span.p-num > a.curr
# def next_page(page_num):
#     input_ele = wait.until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "#J_bottomPage > span.p-skip > input")))
#     submit = wait.until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "#J_bottomPage > span.p-skip > a")))
#     # #J_bottomPage > span.p-num > a:nth-child(3)
#     # #J_bottomPage > span.p-num > a:nth-child(7)
#     input_ele.clear()
#     input_ele.send_keys(page_num)
#     submit.click()
#
#     wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#J_bottomPage > span.p-num > a:nth-child(%s)" %page_num),str(page_num)))
#     # except:
#     #     pass
#     # else:
#     #     wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"J_bottomPage > span.p-num > a.curr"),str(page_num)))


# def main():
    #
    # for page in range(1,101):
    #     index_page(page)
    # bro.close()

def get_products():
    # page_text=bro.page_source
    print("获取到数据")

if __name__ == '__main__':
    # main()
    for page in range(1,101):
        index_page(page)
    # for page_num in range(2,total+1):







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







