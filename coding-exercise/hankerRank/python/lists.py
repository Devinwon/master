"""
https://www.hackerrank.com/challenges/python-lists/problem

insert i e
print 
remove e
append e
sort 
pop 
reverse

"""
if __name__ == '__main__':
	N = int(input())
	lst=[]
	for _ in range(N):
		cmd=input().split()
		if 'insert' in cmd:
			lst.insert(int(cmd[1]),int(cmd[2]))
		elif 'print' in cmd:
			print(lst)
		elif 'pop' in cmd:
			lst.pop()
		elif 'sort' in cmd:
			lst.sort()
		elif 'reverse' in cmd:
			lst.sort(reverse=True)
		elif 'append' in cmd:
			lst.append(int(cmd[1]))
		elif 'remove' in cmd:
			lst.remove(int(cmd[1]))


"""
注意eval的用法
n = input()
l = []
for _ in range(n):
    s = raw_input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print l
"""
