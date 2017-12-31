from bs4 import BeautifulSoup
import requests

url='https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
wb_data=requests.get(url,timeout=30)
soup=BeautifulSoup(wb_data.text,'lxml')
# div.item.name父类
titles=soup.select("div.item.name > a")
imgs=soup.select("img[width='200']")
cates=soup.select("div.detail")
# print(titles[0],imgs[0])

print(cates[0])


'''
def getHTMLtext(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return ''
'''



