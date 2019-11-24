
import requests
from lxml import etree
from urllib import request
import os,time
start_time=time.time()
from multiprocessing.pool import Pool
import schedule
import os
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
}

if not os.path.exists("f:\\tupian"):
    os.mkdir("f:\\tupian")
for i in range(3,4):
    if i ==1:
        print("开始爬取1")
        url="http://pic.netbian.com/4kmeinv/"
        page = requests.get(url=url, headers=headers).text
        tree = etree.HTML(page)
        img_list = tree.xpath("//*[@id='main']/div[3]/ul/li")
        hp = "http://pic.netbian.com"
        for li in img_list:
            img_url = li.xpath("./a/img/@src")[0]
            # title=li.xpath("./a/img/@alt")[0]
            new_url = hp + img_url
            title = new_url.split("/")[-1]
            res = request.urlretrieve(new_url, title)
    else:
        print("开始爬取第%s页" %i)
        url="http://pic.netbian.com/4kmeinv/index_%s.html" %i
        page = requests.get(url=url, headers=headers).text
        tree = etree.HTML(page)
        img_list = tree.xpath("//*[@id='main']/div[3]/ul/li")
        hp = "http://pic.netbian.com"
        for li in img_list:
            img_url = li.xpath("./a/img/@src")[0]
            # title=li.xpath("./a/img/@alt")[0]
            new_url = hp + img_url
            title = new_url.split("/")[-1]

            img_path="f:\\tupian\\"+title +".jpg"
            res = request.urlretrieve(new_url, filename=img_path)

end_time=time.time()
print("结束爬取")
ti=end_time-start_time
print("用时%s" %ti)

# if __name__ == '__main__':
#     p=Pool(50)


