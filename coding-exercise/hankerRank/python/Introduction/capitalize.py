def capitalize(string):
	return ' '.join([x.capitalize() for x in string.split(' ')])


print(capitalize('hello hordl'))