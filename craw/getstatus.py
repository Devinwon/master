import requests

def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		
		# 如果状态不是200，引发异常
		r.raise_for_status
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return "产生异常"

if __name__=="__main__":
	url="http://www.baidu.com"
	print(getHTMLText(url))
