# from appium import webdriver
#
# # 录制
# # el1 = driver.find_element_by_xpath(
# #     "//android.widget.FrameLayout[@content-desc=\"当前所在页面,与的聊天\"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView[1]")
# # el1.click()
# # el2 = driver.find_element_by_xpath(
# #     "//android.widget.FrameLayout[@content-desc=\"当前所在页面,与的聊天\"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.mm.ui.mogic.WxViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout")
# # el2.click()
# # TouchAction(driver).press(x=1041, y=2796).move_to(x=1080, y=476).release().perform()
# #
# # TouchAction(driver).press(x=1176, y=2803).move_to(x=1241, y=849).release().perform()
# from fake_useragent import UserAgent
# import random
# headers = {
#     'User-Agent': UserAgent().random,
# }
#
# # print(headers)
# # print(headers)
# print(headers)
#
# print(dir('a'))
# A=[1,2,4,5,6]
# B=[5,7,8,3,2]
# print(set(A)&set(B))
# print(set(A)^set(B))
# A=('a', 'b', 'c', 'd')
# del A[2]
# import tushare as ts
# import pandas
# df=ts.get_k_data(code="600519",start="2018-11-11")
# print(df)



# import requests
# url="https://v.qq.com/x/cover/zr5a67l333ehzu9.html"
# response=requests.get(url=url).text
#
# print(response)

#
# def bubble_sort(alist):
#     # 外层循环控制比较几轮
#     n = len(alist)
#     for j in range(n - 1):
#         # 内存循环控制交换
#         # -j是不再换已经排好的
#         for i in range(n - 1 - j):
#             # 若前一个比后一个大，则换
#             if alist[i] > alist[i + 1]:
#                 alist[i], alist[i + 1] = alist[i + 1], alist[i]
#
# if __name__ == '__main__':
#     li = [33, 11, 26, 78, 3, 9, 40,4,90,7,56]
#     print(li)
#     bubble_sort(li)
#     print(li)
#
#
dic={'A': 1, 'B.A': 2, 'B.B': 3, 'CC.D.E': 4, 'CC.D.F': 5}
new_dic = {}
for k in dic:
    if "." not in k:
        new_dic[k] = dic[k]
    else:
        li = k.split(".")
        l = len(li)
        now_dic = new_dic
        for i in range(l-1):
            try:
                now_dic[li[i]]
            except:
                now_dic[li[i]] = {}
                now_d = now_dic[li[i]]
                now_dic[li[-1]] = dic[k]





num_list = [6,4,-3,5,-2,-1,0,1,-9]

def sort(arr):
    n = len(arr)
    for i in range(len(arr)):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

sort(num_list)
num_list.reverse()
print(num_list)