# -*- coding:utf-8 -*-
__author__ = 'huposeya'
# 用于获取下载列表

import requests
from bs4 import BeautifulSoup
import paper
import time

def geturllist(list_url):
    responselist = requests.get(list_url)
    soup = BeautifulSoup(responselist.text, 'html.parser')
    urldata = soup.find_all('span', class_="list-identifier")

    list = []
    for i in urldata:
        url = 'http://arxiv.org/' + i('a')[0]['href']
        print('downloading url: %s' % url) # 增加一个提示：正在下载某个页面的数据
        paper_page = paper.papercrawler(url)
        paper_page.downloadpdf()
        print('sleeping 5s...') # 增加下载间隔时间，避免被反爬虫
        time.sleep(5)

        list.append('http://arxiv.org/' + i('a')[0]['href'])
    return list


# main function that call other functions
def main(url):
    geturllist(url)

if __name__ == '__main__':
    url = 'http://arxiv.org/list/cs/recent'
    main(url)