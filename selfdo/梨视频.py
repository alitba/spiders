from selenium import webdriver
import time,requests
import ssl
import os,re
from urllib import request
from lxml import etree
from multiprocessing.dummy import Pool
import schedule
from redis import Redis
import logging
headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }
def get_video():
    url="https://www.pearvideo.com/category_1"
    response=requests.get(url=url,headers=headers).text
    tree=etree.HTML(response)
    li_list=tree.xpath("//*[@id='categoryList']/li")
    v_url_li=[]
    for li in li_list:
        a_tag=li.xpath("./div/a/@href")[0]
        hp="https://www.pearvideo.com/"
        page_url=hp+a_tag
        v_url_li.append(page_url)
    return v_url_li

# get_video()

def parse_vodeo(url):

    response=requests.get(url=url,headers=headers).text
    v_li=re.findall('srcUrl=(.*?),vdoUrl',response)[0]
    v_li = v_li.replace('"', "")
    print(v_li)
    title = v_li.split("/")[-1]
    path="f:\\小视频\\" + title +".mp4"
    if path not in "f:\\小视频\\":
    # request.urlretrieve(v_li,path)
        response2=requests.get(url=v_li,headers=headers).content
        with open(path,"wb") as fp:
            fp.write(response2)
        conn=Redis(host="127.0.0.1",port=6379,db=3)
        res=conn.sadd("livideo",response2)
        if res==1:
            print("有数据更新可爬")
            conn.lpush("video_data",response2)
        else:
            print("暂无更新")
    # print("下载完成")



    # tree=etree.HTML(response)
    # v_url=tree.xpath("//*[@id='JprismPlayer']/video/@src")
    # print(v_url)
    # title =v_url.split("/")[-1]
    # path="f:\\小视频\\" + title +".mp4"
    # request.urlretrieve(v_url,path)


def main():
    star = time.time()
    p = Pool(5)
    p.map(parse_vodeo, get_video())
    end = time.time()
    print(end - star)
    print("over")


def job(message="stuff"):
    print("start working")


if __name__ == '__main__':

    schedule.every().hour.do(job)
    schedule.every().hour.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)











