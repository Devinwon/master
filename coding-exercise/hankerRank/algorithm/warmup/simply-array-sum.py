"""
Given an array of integers, find the sum of its elements.

Function Description

Complete the function which is described by the below function signature.

integer simpleArraySum(integer n, integer_array ar) {
    # Return the sum of all array elements  
}
n:  Integer denoting number of array elements
ar: Integer array with elements whose sum needs to be computed

Raw Input Format
The first line contains an integer,n , denoting the size of the array. 
The second line contains n space-separated integers representing the array's elements.

Sample Input 0
6
1 2 3 4 10 11

Sample Output 0
31

Explanation 0
We print the sum of the array's elements: .
1 +2+ 3+ 4 +10+ 11=31
"""
#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()