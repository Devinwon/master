mon="星期一星期二星期三星期四星期五星期六星期日"
while True:
    i=int(input("请输入星期数字1~7，如7（代表星期日）:"))
    if(8>i>0):
        i=i-1
        i=i*3
        print(mon[i:i+3],"\n")
    else:
        print("Finished")
        break
#done()
