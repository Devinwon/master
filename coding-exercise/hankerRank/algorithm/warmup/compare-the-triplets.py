"""
https://www.hackerrank.com/challenges/compare-the-triplets/problem
"""
#!/bin/python3

import os
import sys

#
# Complete the solve function below.
#
def solve(a0, a1, a2, b0, b1, b2):
    #
    # Write your code here.
    #
    totalofA,totalofB=0,0
    vars=[a0, a1, a2, b0, b1, b2]
    for i in range(3):
      if vars[i]>vars[i+3]:
        totalofA+=1
      elif vars[i]<vars[i+3]:
        totalofB+=1
    return (totalofA,totalofB)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    a0A1A2 = input().split()

    a0 = int(a0A1A2[0])

    a1 = int(a0A1A2[1])

    a2 = int(a0A1A2[2])

    b0B1B2 = input().split()

    b0 = int(b0B1B2[0])

    b1 = int(b0B1B2[1])

    b2 = int(b0B1B2[2])

    result = solve(a0, a1, a2, b0, b1, b2)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
