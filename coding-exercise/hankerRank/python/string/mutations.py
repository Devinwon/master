"""
https://www.hackerrank.com/challenges/python-mutations/problem
modeify by splice
"""
def mutate_string(string, position, character):
	# 可能会越界
	if position==len(string)-1:
		return string[:position]+character
	else:
		return string[:position]+character+string[position+1:]

if __name__ == '__main__':
	s = input()
	i, c = input().split()
	s_new = mutate_string(s, int(i), c)
	print(s_new)