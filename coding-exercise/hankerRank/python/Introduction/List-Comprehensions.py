"""
https://www.hackerrank.com/challenges/list-comprehensions/problem

"""

if __name__ == '__main__':
	x = int(input())
	y = int(input())
	z = int(input())
	n = int(input())
	rel=[]
	for i in range(x+1):
		for j in range(y+1):
			for k in range(z+1):
				temp_lst=[i,j,k]
				if sum(temp_lst)!=n:
					rel.append(temp_lst)
	print(rel)	
