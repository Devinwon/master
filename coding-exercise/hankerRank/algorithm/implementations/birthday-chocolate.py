"""
https://www.hackerrank.com/challenges/the-birthday-bar/problem

"""

#!/bin/python3

import sys

def solve(n, s, d, m):
    # Complete this function
    #return integer
    total=0
    if m<=n:
        for i in range(n-m+1):
            if sum(s[i:i+m])==d:
                total+=1
    return total
        

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)