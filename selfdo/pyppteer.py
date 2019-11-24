import pyppeteer
import asyncio
from pyppeteer import launch

width, height = 1366, 768

#
# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.setViewport({'width': width, 'height': height})
#     await page.goto('https://www.taobao.com')
#     await asyncio.sleep(3)
#
#
# asyncio.get_event_loop().run_until_complete(main())


import asyncio
from pyppeteer import launch


# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto('https://www.taobao.com')
#     await asyncio.sleep(10)
#
#
# asyncio.get_event_loop().run_until_complete(main())
#
# import asyncio
# from pyppeteer import launch
#
#
# async def main():
#     # headless参数设为False，则变成有头模式
#     browser = await launch(headless=False)
#
#     page = await browser.newPage()
#     # 设置页面视图大小
#     await page.setViewport(viewport={'width': 1280, 'height': 800})
#
#     await page.goto('https://www.baidu.com/')
#     # 节点交互
#     await page.type('#kw', '周杰伦', {'delay': 1000})
#     await asyncio.sleep(3)
#     await page.click('#su')
#     await asyncio.sleep(30)
#     # 使用选择器选中标签进行点击
#     alist = await page.querySelectorAll('.s_tab_inner > a')
#     a = alist[3]
#     await a.click()
#     await asyncio.sleep(30)
#     await browser.quit()
#
#
# asyncio.get_event_loop().run_until_complete(main())
import asyncio
from pyppeteer import launch


async def main():
    # headless参数设为False，则变成有头模式

    browser = await launch(headless=False,autoClose=False,args=['--disable-infobars'])

    page = await browser.newPage()
    # 设置页面视图大小
    await page.setViewport(viewport={'width': 1280, 'height': 800})

    await page.goto('https://www.taobao.com/')
    # 节点交互
    await page.type('#q', '冬装', {'delay': 1000})
    await asyncio.sleep(3)
    await page.click('#J_TSearchForm > div.search-button > button')
    await asyncio.sleep(60)
    # 使用选择器选中标签进行点击
    # alist = await page.querySelectorAll('.s_tab_inner > a')
    # a = alist[3]
    # await a.click()
    # await asyncio.sleep(30)
    # await browser.quit()


asyncio.get_event_loop().run_until_complete(main())

