animals={'a': ['aardvark'], 'c': ['coati'], 'b': ['baboon'], 'd': ['donkey', 'dog', 'dingo']}
# animals={}
# animals={'a': [8], 'c': [10, 19, 4, 8, 19, 17, 0, 13, 19, 15], 'b': [9, 4, 10, 15], 'e': [3, 20, 15, 9, 4], 'd': [8, 20, 12, 1, 13, 15, 18]}
# animals={'a':[]}
# print(animals.keys())
# print(animals.values())
'''
aDict: A dictionary, where all the values are lists.

returns: The key with the largest number of values associated with it
'''
# 返回值数量最多对应的key，对k,v同时进行遍历
# 记住以下字典方法：d.keys() d.values() d.items()
# Your Code Here

def biggest(aDict):
	if aDict:
		k=""
		v=""
		for key,value in aDict.items():
			# first replace
			if type(v)==str:
				k=str(key)
				v=value
			elif len(v)<len(value):
				k=str(key)
				v=value
		return k
	else:
		return None
print(biggest(animals))


# def biggest(aDict):
# 	if aDict:
# 		item=""
# 		vue=[]
# 		for key in aDict.keys():
# 			print(aDict[key])
# 			if len(vue)<len(aDict[key]):
# 				item=str(key)
# 				vue=aDict[key]
# 		return item
# 	else:
# 		return None
# print(biggest(animals))



	



	
	