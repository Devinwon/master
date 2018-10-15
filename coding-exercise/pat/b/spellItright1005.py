longstr=input().strip()
allsum=0
for d in longstr:
	allsum+=int(d)


spellsum={0:'zero',
					1:'one',
					2:'two',
					3:'three',
					4:'four',
					5:'five',
					6:'six',
					7:'seven',
					8:'eight',
					9:'nine'}
for v in str(allsum)[:-1]:
	print(spellsum[int(v)],'',end='')
print(spellsum[allsum%10])



	
