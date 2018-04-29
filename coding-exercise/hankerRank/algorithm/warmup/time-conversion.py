"""
https://www.hackerrank.com/challenges/time-conversion/problem
07:05:45PM

19:05:45
"""
#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
		rel=''
		hh=s[:2]
		mmss=s[2:-2]
		if s[-2]=='A':
			if hh=='12':
				rel='00'+mmss
			else:
				rel=s[:-2]
		else:
			if hh=='12':
				rel='12'+mmss
			else:
				rel=str(int(hh)+12)+mmss
		return rel

print(timeConversion('07:05:45AM'))
print(timeConversion('07:05:45PM'))
print(timeConversion('12:00:00AM'))
print(timeConversion('12:00:00PM'))


# if __name__ == '__main__':
#     f = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = timeConversion(s)

#     f.write(result + '\n')

#     f.close()

