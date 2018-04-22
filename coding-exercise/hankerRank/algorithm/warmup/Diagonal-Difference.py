"""
https://www.hackerrank.com/challenges/diagonal-difference/problem
"""
#!/bin/python3

import os
import sys

#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a):
    #
    # Write your code here.
    #
    rel_1,rel_2=0,0
    cnt=len(a)
    for i in range(cnt):
      rel_1+=a[i][i]
      rel_2+=a[i][-(i+1)]
    return abs(rel_1-rel_2)
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()
