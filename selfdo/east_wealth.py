from selenium import webdriver
from lxml import etree
from time import sleep
bro = webdriver.Chrome(executable_path="D:\Chromedriver\chromedriver.exe")

url="http://data.eastmoney.com/zjlx/detail.html"
bro.get(url)

page_text=bro.page_source
tree=etree.HTML(page_text)
fp=open("shres.csv","w",encoding="utf-8")
data_url=tree.xpath("//*[@id='dt_1']//tr")
for texts in data_url:
    order_num= texts.xpath("./td[1]/text()")
    shares_num= texts.xpath("./td[2]/a/text()")
    name= texts.xpath("./td[3]/a/text()")
    now_price= texts.xpath("./td[5]/span/text()")

    order="".join(order_num).strip()
    num="".join(shares_num)
    na="".join(name)
    price="".join(now_price)

    if order and num and na and price:
        fp.write(order+"  "+num+"  "+na+"  "+price+"\n")



fp.close()
print("over")

sleep(2)
bro.close()