import requests
# 找出所有的连接
# 引入库
from bs4 import BeautifulSoup
url="https://www.baidu.com"
try:
	r=requests.get(url)
	r.raise_for_status
	r.encoding=r.apparent_encoding
	demo=r.text
	soup=BeautifulSoup(demo,"html.parser")
	# 迭代先辈
	for link in soup.find_all('a'):
		print(link.get('href')) 



except:
	print("failed")

