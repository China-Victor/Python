# coding=utf-8
"""
 Created by Victor Wu on 2017/12/22.
 
"""
import queue
import re
import threading
from multiprocessing.pool import ThreadPool

import requests

ENCODING = "gb2312"


class DetailTask(threading.Thread):

    def __init__(self, detail_url, lock):
        super().__init__()
        self.lock = lock
        self.detail_url = detail_url

    def write_to_file(self, film):
        self.lock.acquire()  # 加锁，锁住相应的资源
        f = None
        try:
            with open(file="films.txt", mode='a+', encoding=ENCODING) as f:
                newline = str(film) + "\n"
                f.write(newline)
        except Exception as e:
            print(e)
        finally:
            if f is not None:
                f.close()
            self.lock.release()  # 解锁，离开该资源

    def get_films_from_detail(self):
        print("detail : " + self.detail_url)
        req = requests.get(self.detail_url)
        req.encoding = ENCODING
        detail_data = req.text
        urls = re.findall('<a href="(ftp://.*?\.[a-zA-Z0-9]+)">', detail_data)
        print(urls)
        try:
            film = urls.pop(0)
            self.write_to_file(film)
        except Exception as e:
            print(e)

    def run(self):
        self.get_films_from_detail()


class PageTask(threading.Thread):

    def __init__(self, page_url, lock):
        super().__init__()
        self.lock = lock
        self.page_url = page_url

    def get_page_films(self):
        print("page : " + self.page_url)
        req = requests.get(self.page_url)
        req.encoding = ENCODING
        page_data = req.text
        detail_pages = re.findall(r'a href="(.*?)" class="ulink">', page_data)
        threads = []
        for detail in detail_pages:
            dtask = DetailTask("http://www.dytt8.net" + detail, lock=self.lock)
            dtask.setDaemon(True)
            dtask.start()
            print("start dtask " + detail)
            threads.append(dtask)

        for t in threads:
            t.join()

        print("--------------page%s任务已完成--------------" % self.page_url)

    def run(self):
        self.get_page_films()


if __name__ == '__main__':
    write_lock = threading.Lock()
    comm_page_url = "http://www.dytt8.net/html/gndy/dyzz/list_23_%d.html"
    threads = []
    for i in range(1, 10):
        page_url = format(comm_page_url % i)
        pthread = PageTask(page_url=page_url, lock=write_lock)
        pthread.setDaemon(True)
        pthread.start()
        print("start pthread " + str(i))
        threads.append(pthread)

    for t in threads:
        t.join()

    print("-----------所有任务已完成--------------")
