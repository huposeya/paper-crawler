__author__ = 'huposeya'
# -*- coding:utf-8 -*-
#用于获取下载列表

import requests
from bs4 import BeautifulSoup

def geturllist(urllist):
    responselist = requests.get(urllist)
    soup = BeautifulSoup(responselist.text, 'html.parser')
    urldata = soup.find_all('span', class_="list-identifier")
    list = []
    for i in urldata:
        print('http://arxiv.org/' + i('a')[0]['href'])
        list.append('http://arxiv.org/' + i('a')[0]['href'])
    return list


geturllist('http://arxiv.org/list/cs/recent')










