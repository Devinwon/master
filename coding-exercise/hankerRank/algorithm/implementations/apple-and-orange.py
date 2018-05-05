"""
https://www.hackerrank.com/challenges/apple-and-orange/problem

"""
#!/bin/python3

import os
import sys

#
# Complete the countApplesAndOranges function below.
#
def countApplesAndOranges(s, t, a, b, apples, oranges):
    #
    # Write your code here.
    #
    # apple distance
    appleAmount=0
    orangeAmount=0
    for d in apples:
    	if s<=a+d<=t:
    		appleAmount+=1
    for d in oranges:
    	if s<=b+d<=t:
    		orangeAmount+=1
   	print("{0}\n{1}".format(appleAmount,orangeAmount))

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apple = list(map(int, input().rstrip().split()))

    orange = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apple, orange)
