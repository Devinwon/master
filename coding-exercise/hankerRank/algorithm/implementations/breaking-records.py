"""
https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
"""

#!/bin/python3

import os
import sys

#
# Complete the breakingRecords function below.
#
def breakingRecords(score):
    #
    # Write your code here.
    # return [maxNum,minNum]
    maxNum=minNum=0
    maxSet=minSet=score[0]
    for i in range(1,len(score)):
        if score[i]>maxSet:
            maxNum+=1
            maxSet=score[i]
        if score[i]<minSet:
            minNum+=1
            minSet=score[i]
    return [maxNum,minNum]
            
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    score = list(map(int, input().rstrip().split()))

    result = breakingRecords(score)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()