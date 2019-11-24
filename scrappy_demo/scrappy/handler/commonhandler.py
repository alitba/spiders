from gevent import monkey;monkey.patch_all(thread=False)
import gevent
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
import time
from scrappy.models import ScrappyData

invalid_urls = []


class CommonHandler:
    __instance = False

    def __init__(self):
        # option = webdriver.ChromeOptions()
        # option.add_argument("headless")
        # self.driver = webdriver.Chrome(options=option)
        pass

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        cls.__instance = object.__new__(CommonHandler, *args, **kwargs)
        return cls.__instance

    def query(self, dbdata, sam, lock):
    # def query(self, dbdata):
        cid = dbdata.id
        url = dbdata.url
        url_level = dbdata.url_level
        try:
            # 下载网页
            try:
                start = time.time()
                response = urlopen(url)
                page_source = response.read().decode('utf-8')
                # gevent.sleep(0.5)

                # self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
                # 获取当前浏览器的窗口
                # currenttab = self.driver.current_window_handle
                # self.driver.get(url)
                print('geturl' + str(time.time() - start))
                # time.sleep(3)
            except Exception as e:
                invalid_urls.append(url)
                print('下载网页异常', e)
                # 标记当前url处理完毕
                ScrappyData.objects.filter(id=cid).update(flag=4)
                return

            # 解析网页并持久化结果
            try:
                # 当前页面属性持久化
                lock.acquire()
                try:
                    start = time.time()
                    # 切换到新窗口
                    # self.driver.switch_to.window(currenttab)
                    # bsobj = BeautifulSoup(self.driver.page_source, 'lxml')
                    bsobj = BeautifulSoup(page_source, 'lxml')
                    print('page_source' + str(time.time() - start))
                except Exception as e:
                    print('获取网页源码异常')
                finally:
                   lock.release()
                start = time.time()
                title = bsobj.select("html > head > title")
                meta_keywords = bsobj.select("html > head > meta[name='Keywords']")
                if meta_keywords:
                    meta_keywords = bsobj.select("html > head > meta[name='keywords']")

                meta_desc = bsobj.select("html > head > meta[name='description']")
                if meta_desc:
                    meta_desc = bsobj.select("html > head > meta[name='Description']")
                ScrappyData.objects.filter(id=cid).update(
                    title=title[0].text,
                    keywords=meta_keywords[0].attrs['content'] if meta_keywords else '',
                    description=meta_desc[0].attrs['content'] if meta_desc else ''
                )
                # 内容分析并持久化子URL
                links = set()
                aes = bsobj.find_all("a")
                for item in aes:
                    if not item.string:
                        continue
                    else:
                        try:
                            if item.get('href').startswith('http'):
                                links.add(item.get("href"))
                        except:
                            pass
                if len(links) == 0:
                    return

                for link in links:
                    r_dict_tmp = {
                        'parent_id': cid,
                        'url': link,
                        'url_level': url_level+1,
                        'flag': 0}
                    new_url = ScrappyData()
                    new_url.from_dict(r_dict_tmp)
                    new_url.save()
                # 标记当前url处理完毕
                ScrappyData.objects.filter(id=cid).update(flag=2)
                print('parsecontent' + str(time.time() - start))
            except Exception as e:
                print('爬取后的内容入库异常', e)
                # 标记当前url处理完毕
                ScrappyData.objects.filter(id=cid).update(flag=4)
        finally:
            sam.release()