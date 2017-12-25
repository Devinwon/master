# 中间为0的情况，如何处理，需要回退
river_length=int(input())
river_list=list(input().split())
step=0
while river_list and river_list[0]!='0':
    step=step+1
    river_length=river_length-int(river_list[0])
    river_list=river_list[int(river_list[0]):]
if river_list :
    print(-1)
else:
    print(step)