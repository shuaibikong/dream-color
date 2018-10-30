import threading
import time
from queue import Queue
from xml import etree

import requests


class bsSpider:
    def __init__(self):
        self.baseurl = "http://www.budejie.com/"
        self.headers = {"User-Agent":"Mozilla/5.0"}
        #url队列
        self.urlQueue = Queue()
        #响应队列
        self.resQueue = Queue()

    #生成url队列
    def getUrl(self):
        for pNum in range(50):
            url = self.baseurl + str(pNum)
            self.urlQueue.put(url)

    #响应队列
    def getHtml(self):
        while True:
            url = self.urlQueue.get()
            res = requests.get(url, headers=self.headers)
            res.encoding = "urf-8"
            html = res.text
            #放入响应队列
            self.resQueue.put(html)
            #清除此任务
            self.urlQueue.task_done()

    #解析页面
    def content(self):
        while True:
            #从响应队列中以此获取html源码
            html = self.resQueue.get()
            parseHtml = etree.HTML(html)
            r_list = parseHtml.xpath('//div[@class=""j-r-list-c-desc""]/a/text()')
            for r in r_list:
                print(r+"\n")
            self.resQueue.task_done()

    def run(self):
        # 存放所有线程
        thread_list = []
        #获取url队列
        self.getUrl()
        #创建getPage线程
        for i in range(3):
            threadRes = threading.Thread(target=self.getHtml)
            thread_list.append(threadRes)

        #创建xpath解析线程
        for i in range(2):
            threadPath = threading.Thread(target=self.content)
            thread_list.append(threadPath)

        #启用所有线程
        for th in thread_list:
            th.setDaemon(True)

        #如果队列为空, 则执行其它操作
        self.urlQueue.join()
        self.resQueue.join()


if __name__ == "__main__":
    begin = time.time()
    spider = bsSpider()
    spider.run()
    end = time.time()
    print(end - begin)