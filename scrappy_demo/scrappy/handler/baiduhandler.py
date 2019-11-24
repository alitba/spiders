from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup
import time


class BaiduHandler():
    __instance = False

    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        self.driver = webdriver.Chrome(chrome_options=option)

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        cls.__instance = object.__new__(BaiduHandler, *args, **kwargs)
        return cls.__instance

    def query(self, url, keyword):
        result = []
        self.driver.get(url)
        if not keyword:
            keyword = 'InnoDB'
        self.driver.find_element_by_id('kw').send_keys(keyword)
        time.sleep(2)
        self.driver.find_element_by_id('su').send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 10).until(expected_conditions.title_contains(keyword))

        bsobj = BeautifulSoup(self.driver.page_source, 'lxml')
        content = bsobj.text[bsobj.text.index('百度为您找到相关结果'): bsobj.text.index('下一页>') + 4]
        # print(content)

        item_list = bsobj.select('#content_left > div')  # 采用select选择器定位数据
        for item in item_list:
            r_dict = {}
            if len(item.attrs['class']) >= 2 and item.attrs['class'][1] == 'c-container':
                r_dict['title'] = self.get_title(item)
                r_dict['content'] = self.get_content(item)
                r_dict['link'] = self.get_link(item)
            result.append(r_dict)

        return result

    @staticmethod
    def get_title(item):
        title = ''
        for c in item.contents:
            try:
                if c.attrs['class'][0] == 't':
                    title = c.text.strip()
                    break
            except:
                pass
        return title

    @staticmethod
    def get_content(item):
        content = ''
        for c in item.contents:
            try:
                if c.attrs['class'][0] == 'c-abstract':
                    content = c.text.strip()
                    break
            except:
                pass
        return content

    @staticmethod
    def get_link(item):
        link = ''
        for c in item.contents:
            try:
                if c.attrs['class'][0] == 't':
                    link = c.contents[0].attrs['href'].strip()
                    break
            except:
                pass
        return link
