# -*- coding:utf-8 -*-
__author__ = 'huposeya'
# 用于多页连续下载

from bs4 import BeautifulSoup
import requests
import re
import list


# 获取total条目及构建多个单页下载列表组成的list
def get_total(url_total):
    try:
        response = requests.get(url_total)
    except requests.HTTPError as e:
        if hasattr(e, 'reason'):
            print('连接失败,错误原因', e.reason)
        else:
            print('连接失败, 未知原因')
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # 正则不熟，bs加正则提取total数
    urldata = soup.find('small')
    pattern = re.compile(r'.*?of (.*?) entries.*?', re.S)
    items = re.match(pattern, urldata.get_text()).group(1)


    #构建多个单页下载列表组成的list
    b = int(items)/25+1
    list_url = []
    for i in range(int(b)):
        url_a = 'http://arxiv.org/list/' + 'cs.CL' + '/pastweek?skip=' + str(i) + '&show=25'
        # url = 'http://arxiv.org/list/' + '缩写' + '/pastweek?skip=' + '批次索引' +'&show=25'
        list_url.append(url_a)
    # print(list_url)
    return list_url


# 以list的形式连续多页下载
def download_list_pdf():
    l = get_total(url)
    for i in range(len(l)):
        print('总计' + str(len(l)) + '批url_list,该批为第' + str(i + 1) + '批url_list:', l[i])
        list.main(l[i]) # 调用list.py下载pdf



def main(url):
        get_total(url)
        download_list_pdf()

if __name__ == '__main__':
    url = 'http://arxiv.org/list/' + 'cs.CL' + '/pastweek?skip=0&show=25'
    # url = 'http://arxiv.org/list/' + '缩写' + '/pastweek?skip=0&show=25'
    main(url)