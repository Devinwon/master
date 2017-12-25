import requests
import os

url="http://site.ip138.com/"
# print(r.url)
# 人工都是以网址的形式提交
try:
	r=requests.get(url+'202.204.80.112'+'/')
	r.raise_for_status
	r.encoding=r.apparent_encoding
	print(r.text)
except:
	print("failed")

