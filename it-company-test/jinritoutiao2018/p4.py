key=input()
doc=input()
keyOrder=[]
docpy=doc[:]
score=100
for v in key:
	if v in docpy:
		if keyOrder and docpy.index(v)+len(doc)-len(docpy)>keyOrder[-1]:
			keyOrder.append(docpy.index(v)+len(doc)-len(docpy))
			docpy=docpy[docpy.index(v):]
		elif not keyOrder:
			keyOrder.append(doc.index(v))
			docpy=docpy[docpy.index(v):]
		else:
			score=0
			break
	else:
		score=0
		break
if score:
	if len(keyOrder)>1:
		for i in range(len(keyOrder)-1):
			score-=(keyOrder[i+1]-keyOrder[i]-1)

print(score)


