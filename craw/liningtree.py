import requests
# 平行遍历
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
	print(soup.a.next_sibling.next_sibling)
	print(soup.a.privious_sibling)

	'''
	循环遍历后续节点
	for sibling in soup.a.next_siblings:
		print(sibling)

	循环遍历前续节点
	for sibling in soup.a.privious_siblings:
		print(sibling)

	'''

except:
	print("failed")

