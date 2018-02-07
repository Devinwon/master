s="hello"
print(s.upper())
print(s)

print(s.isupper())

print('Hello'.isalpha())
print('Hello'.isdecimal())
print('123'.isalnum())
print('hello'.isalnum())
print('hello123'.isalnum())
print('hello123$'.isalnum())

print("-"*10)
print('   '.isspace())
print('\t'.isspace())

print("-"*10)
print('hello123$'.isalnum())

print("-"*10)
print('Hello'.istitle())
print('HELLO'.istitle())
print('hello'.istitle())

print("-"*10)
print(("Hello world").startswith("hello"))
print(("Hello world").endswith("rld"))

print("-".join(['a','b','c']))


print("-"*10)

print("My name is Devin".split())
print("My_name_is_Devin".split('_'))

print("-"*10)

print("Hello".rjust(8))
print("Hello".ljust(8))
print("Hello".center(8))
print("Hello".ljust(8,'#'))

print("-"*10)
print("  hello world  ".strip(),'###',sep='')
print("  hello world  ".lstrip(),'###',sep='')
print("  hello world  ".rstrip(),'###',sep='')
