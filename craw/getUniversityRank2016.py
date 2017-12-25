#CrawUnivRankingA.py
# 2015、2016爬取大学排名
import requests
from bs4 import BeautifulSoup
import bs4
 
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
 
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            print(tds)
            break
            # print(type(tds))
            # ulist.append([tds[0].string, tds[1].string, tds[3].string])
 
def printUnivList(ulist, num):
    print("{:^10}\t{:<20}\t{:<10}".format("排名","学校名称","总分"))
    # print("{:*^10}\t{:*<20}\t{:*<10}".format("RANK","NAME","MARKS"))
    for i in range(num):
        u=ulist[i]
        print("{:^10}\t{:<15}\t{:<10}".format(u[0],u[1],u[2]))
     
def main():
    uinfo = []
    # http://www.zuihaodaxue.cn/zuihaodaxuepaiming2015_0.html
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    # printUnivList(uinfo, 10) # 20 univs
main()