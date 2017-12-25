import requests
import time

success_cnt=0
fail_cnt=0


def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)

		# 如果状态不是200，引发异常
		r.raise_for_status
		return True
	except:
		return False


# if __name__=="__main__":
url="http://www.baidu.com"
start=time.time()
while success_cnt<100:
	if getHTMLText(url):
		success_cnt+=1
		print(success_cnt+fail_cnt,"success")
	else:
		print(success_cnt+fail_cnt,"fail")
		fail_cnt+=1
end=time.time()	
print("耗时:",end-start)
