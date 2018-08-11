"""
>>> applyCoder("Hello, world!", buildCoder(3))
'Khoor, zruog!'
>>> applyCoder("Khoor, zruog!", buildCoder(23))
'Hello, world!'
"""
def buildCoder(shift):
	"""
	Returns a dict that can apply a Caesar cipher to a letter.
	The cipher is defined by the shift value. Ignores non-letter characters
	like punctuation, numbers and spaces.

	shift: 0 <= int < 26
	returns: dict
	"""
	### TODO.
	# return "Not yet implemented." # Remove this comment when you code the function
	dic={}
	lcase="abcdefghijklmnopqrstuvwxyz"
	ucase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for l in lcase:
	    dic[l]=chr((ord(l)+shift-97)%26+ord('a'))
	for u in ucase:
	    dic[u]=chr((ord(u)+shift-65)%26+ord('A'))
	return dic


def applyCoder(text, coder):
	"""
	Applies the coder to the text. Returns the encoded text.

	text: string
	coder: dict with mappings of characters to shifted characters
	returns: text after mapping coder chars to original text
	"""
	### TODO
	finalText=""
	for v in text:
		if v.isalpha():
			finalText+=coder[v]
		else:
			finalText+=v
	return finalText

print applyCoder("Hello, world!", buildCoder(3))
print applyCoder("Khoor, zruog!", buildCoder(23))




