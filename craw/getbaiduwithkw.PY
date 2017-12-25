import requests
kv={"wd":"Python"}
url="http://www.baidu.com/s"
try:
	r=requests.get(url,params=kv)
	r.raise_for_status
	print(len(r.text))
except:
	
	print("failed")

