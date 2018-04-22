"""
https://www.hackerrank.com/challenges/staircase/problem
"""
#!/bin/python3

import os
import sys

#
# Complete the staircase function below.
#
def staircase(n):
    #
    # Write your code here.
    #
    for i in range(n):
    	print(' '*(n-i-1),'#'*(i+1),sep='')

if __name__ == '__main__':
    n = int(input())

    staircase(n)