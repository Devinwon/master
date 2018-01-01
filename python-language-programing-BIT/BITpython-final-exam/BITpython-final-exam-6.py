'''
凯撒加密
大小写字母加密，其他不管
'''
src=input()
dst=""
for v in src:
	if v.isalpha():
		if v.islower():
			dst+=chr(((ord(v)+3-ord('a')))%26+ord('a'))
		else:
			dst+=chr(((ord(v)+3-ord('A')))%26+ord('A'))
	else:
		dst+=v
print(dst)

'''
src=input()
dst=""
for v in src:
	if v.isalpha():
		if v.islower():
			if v<='w':
				dst+=chr((ord(v)+3))
			else:
				dst+=chr((ord(v)+3)%122+96)
		else:
			if v<='W':
				dst+=chr((ord(v)+3))
			else:
				dst+=chr((ord(v)+3)%90+64)
	else:
		dst+=v
print(dst)
'''
