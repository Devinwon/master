import requests
url="https://www.amazon.com/gp/product/B01M8L5Z3Y"
kv={"user-agent":"Mozilla/5.0"}
try:
	r=requests.get(url,headers=kv)
	r.raise_for_status
	print(r.text[:1000])
except:
	print(r.request.headers)
	print("failed")

