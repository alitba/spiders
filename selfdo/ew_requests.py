import requests,json
from urllib.parse import urlencode
from redis import Redis
import re,random
from fake_useragent import UserAgent

def get_data(page):
    global response
#pn=4&pz=50&po=1&np=1&ut=b2884a393a59ad64002292a3e90d46a5&fltt=2&invt=2&fid0=f4001&fid=f62&fs=m:0+t:6+f:!2,m:0+t:13+f:!2,m:0+t:80+f:!2,m:1+t:2+f:!2,m:1+t:23+f:!2,m:0+t:7+f:!2,m:1+t:3+f:!2&stat=1&fields=f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124&rt=52362467&cb=jQuery18307851703872273994_1570874002862&_=1570874024258
    params={
        "pn": page,
        "pz": 50,
        "po": 1,
        "np": 1,
        "ut": "b2884a393a59ad64002292a3e90d46a5",
        "fltt": 2,
        "invt": 2,
        "fid0": "f4001",
        "fid": "f62",
        "fs": "m:0 t:6 f:!2,m:0 t:13 f:!2,m:0 t:80 f:!2,m:1 t:2 f:!2,m:1 t:23 f:!2,m:0 t:7 f:!2,m:1 t:3 f:!2",
        "stat":1,
        "fields": "f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124",
        "rt": 52362778,
        "cb": "jQuery18307002612467676985_1570875728536",
        "_": 1570883362516
    }

    url="http://push2.eastmoney.com/api/qt/clist/get?"+urlencode(params)

    headers={
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
        "User-Agent":UserAgent().random
    }
    response=requests.get(url=url,headers=headers).text
    # res=json.loads(response)
    # print(res,type(res))
    # res2=response.get("data")
    # print(res2)
    # print(res)

    # print(response)
    # un=re.findall('jQuery.*?"diff":\[',response)[0]
    # response=response.replace(un,"")
    # response=response.replace("]}})","")
    print(response)
    # res = dict(response)
    # print(res)
    # # 股票名称
    # name = res["data"]["diff"][0]["f14"]
    # print("当前第%s页" %page + "\n" +response)
    # print(name)




    # return response

conn=Redis(host="127.0.0.1",port=6379,db=2)

for page in range(1,2):
     get_data(page)
     conn.lpush("shares",response)

print("完成")
