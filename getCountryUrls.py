#-*-coding:utf-8-*-
import re, urllib2

#抓取网页
def getHtml(url):
    header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'}
    request = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(request)
    html = response.read()
    return html

#爬取每个页面上国家的链接
def getCountryUrl(html):
    pattern = re.compile('<a href="/places/default/view/(.*?)">')
    items = re.findall(pattern, html)
    for urls in items:
        print 'http://example.webscraping.com/places/default/index/'+urls

#递归爬取每页面国家的链接
def crawler(page):
    if page > 25:
        exit()
    page_url = 'http://example.webscraping.com/places/default/index/%d' % page
    page += 1
    try:
        html = getHtml(page_url)
        getCountryUrl(html)
        crawler(page)
    except Exception, e:
        print e
        crawler(page)

if __name__ == '__main__':
    crawler(0)
