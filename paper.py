# -*- coding:utf-8 -*-
__author__ = 'huposeya'
# 单页文章的下载，以标题.pdf的形式保存

import requests
from bs4 import BeautifulSoup


class papercrawler:
    def __init__(self, url):
        self.url = url

    # 获取基本信息
    def get_basic_info(self):
        try:
            print('requesting %s' % self.url) # 增加一个提示，程序正在发送请求
            response = requests.get(self.url)
        except requests.HTTPError as e:
            if hasattr(e, 'reason'):
                print('连接失败,错误原因', e.reason)
            else:
                print('连接失败, 未知原因')
            return None # 无论是否捕捉到异常，都有返回

        soup = BeautifulSoup(response.text, 'html.parser')

        titledata = soup.select('meta[name="citation_title"]')
        self.title = titledata[0]['content']
        # 变量前加self.可传递至其他function（）
        urlpagedata = soup.select('meta[name="citation_pdf_url"]')
        self.pdf_url = urlpagedata[0]['content']

        return soup

    # 下载pdf到本地
    def downloadpdf(self):
        self.get_basic_info()
        responsepage = requests.get(self.pdf_url)

        pdfname = str(self.title) + '.pdf'
        with open(pdfname, 'wb') as f:
            f.write(responsepage.content)


def main(url):
    paper = papercrawler(url)
    paper.downloadpdf()

if __name__ == '__main__':
    url = 'http://arxiv.org/abs/1608.07531'
    main(url)