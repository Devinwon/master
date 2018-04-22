"""
https://www.hackerrank.com/challenges/plus-minus/problem
"""
#!/bin/python3

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    #
    # Write your code here.
    #
    postive_fraction,negative_fraction,zero_fraction=0,0,0
    for v in arr:
      if v>0:
        postive_fraction+=1
      elif v<0:
        negative_fraction+=1
      else:
        zero_fraction+=1  
    print("{:.6f}".format(postive_fraction/len(arr)))
    print("{:.6f}".format(negative_fraction/len(arr)))
    print("{:.6f}".format(zero_fraction/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
