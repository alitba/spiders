# import requests
# from selenium import webdriver
# # url="http://tyst.migu.cn/public/ringmaker01/n17/2017/07/%E6%97%A0%E6%8D%9F/2009%E5%B9%B406%E6%9C%8826%E6%97%A5%E5%8D%9A%E5%B0%94%E6%99%AE%E6%96%AF/flac/%E4%B8%83%E9%87%8C%E9%A6%99-%E5%91%A8%E6%9D%B0%E4%BC%A6.flac"
# # res=requests.get(url)
# # print(res)
# # bro=webdriver.Chrome(executable_path="D:\Chromedriver\chromedriver.exe")
# # headers={
# # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
# # }
# #
# #
# #
# #
# #
# # for i in range(1,2):
# #     url=("http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=ct&st=(BalFlowMain)&sr=-1&p='{}'&ps=50&js=var\%20YHXKgVvH=\{pages:(pc),date:%222014-10-22%22,data:[(x)]}&token=894050c76af8597a853f5b408b759f5d&cmd=C._AB&sty=DCFFITA&rt=52348162").format(i)
# #     response=requests.get(url=url,headers=headers).text
# #     print(response)
#
#
#
# # data="U2FsdGVkX19DXMzPLizVK2rHawU6CEyzwst4Z5d47gp9em75y/7cUPn4AQS46VbqlVGebLLnuOzUxTUx6nTHQg=="
# # print(data.encode())
#
# import pprint
# import requests
# import re
# from urllib.parse import urlencode
# # # for page in range(1,78):
# # headers={
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
# # }
# # params={
# #     "type": "ct",
# #     "st": "(BalFlowMain)",
# #     "sr": -1,
# #     "p": 1,
# #     "ps": 50,
# #     "js": 'var XsJPKfme={pages:(pc),date:"2014-10-22",data:[(x)]}',
# #     "token": "894050c76af8597a853f5b408b759f5d",
# #     "cmd": "C._AB",
# #     "sty": "DCFFITA",
# #     "rt": 52358499,
# # }
# # url="http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?"+urlencode(params)
# #
# # response=requests.get(url=url,headers=headers).headers
# # pprint.pprint(response)
#
# # response2=requests.get(url=url,headers=headers)
# #
# # print(response2)
#
#
# # from selenium import webdriver
# # from time import sleep
# #
# #
# # bro = webdriver.Chrome(executable_path="D:\Chromedriver\chromedriver.exe")
# #
# # # url="http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=ct&st=(BalFlowMain)&sr=-1&p=3&ps=50&js=var%20fEeYGLNI={pages:(pc),date:%222014-10-22%22,data:[(x)]}&token=894050c76af8597a853f5b408b759f5d&cmd=C._AB&sty=DCFFITA&rt=52358673"
# # url="http://data.eastmoney.com/zjlx/detail.html"
# # bro.get(url=url)
# #
# # page_text=bro.page_source
# # print(page_text)
# #
# #
# # sleep(5)
# # bro.close()
#
#
# #J_bottomPage > span.p-skip > input
#
# # url="http://play.taihe.com/?__m=mboxCtrl.playSong&__a=606889413&__o=/search||songListIcon&fr=-1||-1&__s=%E7%A8%BB%E9%A6%99#"
# #
# # response3=requests.get(url=url,headers=headers)
# # pprint.pprint(response3.json())
#
# # dict={
# #     "a":1,
# #     "b":2
# # }
# # print(dict)
# # pprint.pprint(dict)
#
#
#
# # url="http://music.migu.cn/v3/api/music/audioPlayer/getPlayInfo?dataType=2&data=U2FsdGVkX1%2FLdPEAQHq8kfZnoilsTXSzCclXXLtzKwdxQVAgftRSmlpKBw0d2DUENgqxSAFzE2eZAytM3CvqqA%3D%3D&secKey=jOfuXkdPYj5DFtqYPyLU4A9fsp99hcdmATw%2F2X0u6unXObPnXayUPM7JGclX66QiPxAZtkDVdsL112jsHwmEVUyhIm871Si29fKih7PD%2Bk%2FaWhNDbzezqVj32e5zT1qE8ZGGxi1NSTalpGKFWWkQvVCCyaukQATKRcqXRjzVxiY%3D"
# #
# #
# # headers={
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
# # }
# #
# # response=requests.get(url=url,headers=headers)
# # print(response.json())#为什么不能json？
#
#
#
# #
# # data={
# #     "songIds": "273584",
# #     "hq": "0",
# #     "type": "m4a,mp3",
# #     "rate":"",
# #     "pt": "0",
# #     "flag": "-1",
# #     "s2p": "-1",
# #     "prerate": "-1",
# #     "bwt": "-1",
# #     "dur": "-1",
# #     "bat": "-1",
# #     "bp": "-1",
# #     "pos": "-1",
# #     "auto": "-1",
# # }
# # %E6%97%A0%E6%8D%9F/2016%E5%B9%B45%E6%9C%8830%E5%8F%B7%E6%97%A0%E6%8D%9F%E6%95%B0%E6%8D%AE%E8%A1%A5%E5%85%85/flac/%E6%9D%8E%E7%99%BD-%E6%9D%8E%E8%8D%A3%E6%B5%A9
# # url="http://play.taihe.com/data/music/songlink"
# #
# # response=requests.post(url=url,data=data)
# #
# # print(response.json())
#
# # res=urlencode("%E6%97%A0%E6%8D%9F/2016%E5%B9%B45%E6%9C%8830%E5%8F%B7%E6%97%A0%E6%8D%9F%E6%95%B0%E6%8D%AE%E8%A1%A5%E5%85%85")
# # print(res)
#
# import redis
# print(redis.VERSION)


from selenium import webdriver