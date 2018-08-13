longest=""
def ordered(s):
	l=len(s)
	for inx in range(l-1):
		if s[inx]>s[inx+1]:
			return False
	return True

inilen=len(s)
if inilen==1:
	longest=s
elif inilen>1:
	sublen=inilen
	while sublen>1:
		offset=inilen-sublen
		while offset>=0:
			for inx in range(offset+1):
				sub=s[inx:inx+sublen]
				if ordered(sub) and len(sub)>len(longest):
					longest=sub   
			offset-=1
		sublen-=1

if not longest:
	longest=s[0]
print(("Longest substring in alphabetical order is: {}").format(longest))