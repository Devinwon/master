#-*- coding:utf-8 -*-
import requests
import time

success_cnt=0
fail_cnt=0

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        # 状态码200OK，否则返回错误
        r.raise_for_status
        return True
    except:
        return False

# if __name__=="__main__":
url="http://www.baidu.com"
start=time.time()
while success_cnt<10:
    if getHTMLText(url):
        success_cnt+=1
        print(success_cnt+fail_cnt,"success")
    else:
        print(success_cnt+fail_cnt,"fail")
        fail_cnt+=1
end=time.time() 
print("success",success_cnt)
print("fail",fail_cnt)   
print("total time:",end-start)
