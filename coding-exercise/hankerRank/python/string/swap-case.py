"""
https://www.hackerrank.com/challenges/swap-case/problem
"""
def swap_case(s):
	rel=''
	for v in s:
		if 'A'<=v<='Z':
			rel+=v.lower()
		elif 'a'<=v<='z':
			rel+=v.upper()
		else:
			rel+=v
	return rel

if __name__ == '__main__':
	s = input()
	result = swap_case(s)
	print(result)


