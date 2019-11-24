from selenium import webdriver
from time import sleep
from lxml import etree
bro = webdriver.Chrome(executable_path="D:\Chromedriver\chromedriver.exe")
url = "https://www.iqiyi.com/a_19rrh2ylud.html?vfrm=pcw_home&vfrmblk=B&vfrmrst=fcs_0_t12"
bro.get(url)

page_text = bro.page_source
print(page_text)
print("<==============>")
tree=etree.HTML(page_text)
data = tree.xpath("//*[@id='flashbox']/div[3]/video")
print(data)



