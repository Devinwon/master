
s = 'azcbobobegghakl'
vol=['a','e','i','o','u']
total=0
for v in s:
	if v in vol:
		total+=1
print "Number of vowels: {0}".format(total)
