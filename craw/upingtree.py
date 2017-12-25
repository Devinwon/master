import requests
# 向上遍历
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
	for parent in soup.a.parents:
		if parent is None:
			print(parent)
		else:
			print(parent.name)

except:
	print("failed")

