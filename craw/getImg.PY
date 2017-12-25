import requests
import os

url="https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1507982382&di=80932045c14dafdfb223bc58f8cb76e1&src=http://www.zhlzw.com/UploadFiles/Article_UploadFiles/201204/20120412123914329.jpg"
root="F://python//"
# use original filename
path=root+url.split('/')[-1]

try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r=requests.get(url)
		with open(path,'wb') as f:
			f.write(r.content)
			f.close()
			print("file saved")
	else:
		print("file exits")
except:
	print("get file failed")

