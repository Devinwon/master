animals={'a': ['aardvark'], 'c': ['coati'], 'b': ['baboon'], 'd': ['donkey', 'dog', 'dingo']}
print(animals.values())
cnt=0
for v in animals.values():
    cnt+=len(v)
print(cnt)