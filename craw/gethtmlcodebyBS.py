import requests
# 引入库
from bs4 import BeautifulSoup
url="https://www.baidu.com"
try:
	r=requests.get(url)
	r.raise_for_status
	r.encoding=r.apparent_encoding
	demo=r.text
	# BeautifulSoup("待解析对象","html.parser")
	soup=BeautifulSoup(demo,"html.parser")
	# # print(soup.prettify())
	# # string获取标题内容
	# print(soup.title.string)
	# type(soup.title.string)
	# # 根据类型判断是否注释comment
	# tag=soup.a
	# print(tag.parent.parent.name)
	# print(tag.attrs)
	# print(tag.attrs['class'])
	# print(tag.attrs['href'])

# 返回包含的儿子
	# print(soup.head.contents)

	# 儿子shul
	# print(len(soup.head.contents))
	
	# 最后一个儿子
	# print(soup.head.contents[-1])
	# print(soup.body.contents)
# 遍历儿子节点
	for child in soup.head.children:
		print(child)
except:
	print("failed")

