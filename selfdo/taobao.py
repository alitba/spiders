# # import pymongo
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from pyquery import PyQuery as pq
#
# from urllib.parse import quote
# from redis import Redis
from selenium.webdriver.chrome.options import Options
#
# import time
# # browser = webdriver.Chrome()
# # browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
# options=Options()
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# browser = webdriver.Chrome(executable_path="D:\Chromedriver\chromedriver.exe",options=options)
#
# KEYWORD = 'ipad'
#
# MAX_PAGE = 100
# wait = WebDriverWait(browser, 10)
# # client = pymongo.MongoClient(MONGO_URL)
# # db = client[MONGO_DB]
#
#
# def index_page(page):
#     """
#     抓取索引页
#     :param page: 页码
#     """
#     print('正在爬取第', page, '页')
#     try:
#         url = 'https://www.taobao.com/'
#         browser.get(url)
#         time.sleep(5)
#
#         input = wait.until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
#         submit = wait.until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
#         input.clear()
#         time.sleep(2)
#         input.send_keys(KEYWORD)
#         time.sleep(5)
#         submit.click()
#         # wait.until(
#         #     EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
#         # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
#         get_products()
#     except TimeoutException:
#         index_page(page)
#
#
# def next_page(page):
#     input = wait.until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
#     submit = wait.until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
#     input.clear()
#     input.send_keys(page)
#     submit.click()
#     wait.until(
#         EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'), str(page)))
#     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
#
#
#
# def get_products():
#     """
#     提取商品数据
#     """
#     html = browser.page_source
#     doc = pq(html)
#     items = doc('#mainsrp-itemlist .items .item').items()
#     for item in items:
#         product = {
#             'image': item.find('.pic .img').attr('data-src'),
#             'price': item.find('.price').text(),
#             'deal': item.find('.deal-cnt').text(),
#             'title': item.find('.title').text(),
#             'shop': item.find('.shop').text(),
#             'location': item.find('.location').text()
#         }
#         print(product)
#         conn = Redis(host="127.0.0.1", port=6379)
#         conn.lpush(product)
#
#
# # def save_to_redis(result):
# #     """
# #     保存至MongoDB
# #     :param result: 结果
# #     """
#
#
#
# def main():
#     """
#     遍历每一页
#     """
#     for i in range(1,  MAX_PAGE+ 1):
#         index_page(i)
#     browser.close()
#
#
# if __name__ == '__main__':
#     main()



import os
import pickle
import time
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
options=Options()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
brower = webdriver.Chrome(executable_path="D:\Chromedriver\chromedriver.exe",options=options)
wait = WebDriverWait(brower, 10)
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
kw=brower.find_element_by_css_selector("#q")
kw.send_keys("男大衣")
time.sleep(1)
ensure=brower.find_element_by_css_selector("#J_TSearchForm > div.search-button > button")
ensure.click()
target=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_Itemlist_Pic_602592656575")))

target.click()

windows=brower.window_handles
brower.switch_to.window(windows[1])
style=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_DetailMeta > div.tm-clear > div.tb-property > div > div.tb-key > div > div > dl:nth-child(1) > dd > ul > li:nth-child(2) > a")))
style.click()
# size=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_DetailMeta > div.tm-clear > div.tb-property > div > div.tb-key > div > div > dl.tb-prop.tm-sale-prop.tm-clear.tm-img-prop > dd > ul > li > a > span")))
# size.click()
time.sleep(2)
buy=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_LinkBuy")))
buy.click()
time.sleep(2)
queding=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#submitOrderPC_1 > div > a")))
queding.click()

password=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#payPassword_container > div")))
password.send_keys("111111")

pay=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_authSubmit")))
pay.click()