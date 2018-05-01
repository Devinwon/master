"""
字串在母川中出现的次数
left->right

"""

def count_substring(string, sub_string):
	sub_len=len(sub_string)
	cnt=0
	if sub_len<=len(string):
		for i in range(0,len(string)-sub_len+1):
			if string[i:sub_len+i]==sub_string:
				cnt+=1
	return cnt



if __name__ == '__main__':
	string = input().strip()
	sub_string = input().strip()

	count = count_substring(string, sub_string)
	print(count)