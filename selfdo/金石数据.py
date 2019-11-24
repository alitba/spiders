import requests
from lxml import etree
import re
from selenium import webdriver
bro = webdriver.Chrome(executable_path="D:\Chromedriver\chromedriver.exe")
url="https://www.jin10.com/"
bro.get(url=url)
page=bro.page_source
print(page)
p_list=re.findall('<p class="J_flash_text">(.*?)</p>',page)
print(p_list)
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
# }
# def get_data():
#     url="https://www.jin10.com/"
#     page_text=requests.get(url=url,headers=headers).text
#     # print(page_text)
#     tree=etree.HTML(page_text)
#     news_list=tree.xpath("//*[@id='J_flash_wrap2019-10-25']")
#     print(news_list)
#     # for div_list in news_list:
#     #     news=div_list.xpath(".//p")
#
# get_data()