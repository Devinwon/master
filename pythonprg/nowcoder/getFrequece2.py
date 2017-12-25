words=list(input().split())
for val in words:
	if words.count(val)>=len(words)//2:
		print(val)
		break