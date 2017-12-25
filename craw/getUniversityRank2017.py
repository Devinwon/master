#CrawUnivRankingA.py
# 2017爬取大学排名,有些不规范，需要修改
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

            # univerRankstr=str(tds[0])
            # print(univerRankstr.split('<td>')[1])
            # break
            # 针对2017以下部分有修改
            ulist.append([str(tds[0]).split('<td>')[1], tds[1].string, tds[3].string])

 
def printUnivList(ulist, num):
    print("{:^10}\t{:<20}\t{:<10}".format("排名","学校名称","总分"))
    # print("{:*^10}\t{:*<20}\t{:*<10}".format("RANK","NAME","MARKS"))
    for i in range(num):
        u=ulist[i]
        print("{:^10}\t{:<15}\t{:<10}".format(u[0],u[1],u[2]))
     
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 10) # 20 univs
main()