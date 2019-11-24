# from gevent import monkey;monkey.patch_all(thread=False)
from concurrent import futures
from threading import Semaphore
from threading import Lock
# import gevent
import time
from scrappy.models import ScrappyData, Config
from scrappy.handler.commonhandler import CommonHandler


def task():
    ch = CommonHandler()
    level = Config.objects.filter(key='max_level')[0].value
    thread_pool = futures.ThreadPoolExecutor(30)
    sam = Semaphore(20)
    lock = Lock()

    while True:
        # 查询数据库有没有flag=False的数据，有就取第一条，用于后台守护进程调用
        dbdata = ScrappyData.objects.filter(flag=0, url_level__lte=level).order_by('id')[:5]
        if len(dbdata) == 0:
            time.sleep(1)
            continue

        for i in range(len(dbdata)):

            if ScrappyData.objects.filter(id=dbdata[i].id).update(flag=1) == 0:
                continue
            sam.acquire()
            thread_pool.submit(ch.query, dbdata[i], sam, lock)
            # gevent.spawn(ch.query, dbdata[i])