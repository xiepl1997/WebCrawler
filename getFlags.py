#-*- coding:utf-8 -*-
#rate: 0.1
#burst: 3
#用来爬取爬虫示例网站上的国家的国旗

import urllib, urllib2, re
from bs4 import BeautifulSoup
import time

def getHtml(url):
    header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'}
    request = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(request)
    html = response.read()
    html2 = BeautifulSoup(html, 'html.parser')
    return html2

def getFlags(html, a):
    flagurls = []
    flags = html.find_all('img')
    for pattern in flags:
        flagurls.append('http://example.webscraping.com'+pattern.get('src'))
    for i in flagurls:
        urllib.urlretrieve(i, '/home/xpl/图片/Flags/%d.png'%a)
        a += 1
    return a

if __name__ == '__main__':
    a = 1
    for i in range(0, 25):
        time.sleep(2)
        url = 'http://example.webscraping.com/places/default/index/%d'%i
        html = getHtml(url)
        a = getFlags(html, a)
