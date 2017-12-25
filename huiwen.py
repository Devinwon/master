#-*- coding:utf-8 -*-
'''
b插入中构成回文
'''
from _tracemalloc import start
def ishuiwen(s):
    flag=True
    for index in range(len(s)//2):
        if s[index]!=s[-(index+1)]:
            flag=False
            break
    return flag

stra=input()
strb=input()
rel=[]
start=0
while start<=len(stra):
    temp=''
    if start==0:
        temp=strb+stra   
        start+=1       
        if ishuiwen(temp):
#             print('y1')
            rel.append(temp)
    elif start>0 and start<len(stra):
        temp=stra[:start]+strb+stra[start:]
        start+=1
        if ishuiwen(temp):
#             print('y2')
            rel.append(temp)
    else:      
        temp=stra+strb
        start+=1
        if ishuiwen(temp):
#             print('y3')
            rel.append(temp)    
print(len(rel))
