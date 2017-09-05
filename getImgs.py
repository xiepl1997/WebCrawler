#在猫扑网上爬取一些好看的～图片
#-*-coding:utf-8-*-
import urllib2, re, urllib
from bs4 import BeautifulSoup

def getHtml(url):
    header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'}
    request = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(request)
    html = response.read()
    return html

def getImg(html):
    x = 1
    imgUrls = []
    html = BeautifulSoup(html, 'html.parser')
    imgs = html.find_all('p', class_="tc mb10")
    for i in imgs:
        temp = i.find('img')
        link = temp.get('src')
        imgUrls.append('http:'+link)
    for i in imgUrls:
        urllib.urlretrieve(i, '/home/xpl/图片/%d.jpg'%x)
        x += 1

if __name__ == '__main__':
    url = 'http://tt.mop.com/a/170905093348712403573.html'
    html = getHtml(url)
    getImg(html)
