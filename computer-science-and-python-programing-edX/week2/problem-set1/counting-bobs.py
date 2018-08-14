# Paste your code into this box 
cnt=0
src="bob"
while True:
    if src in s:
        cnt+=1
        index=s.index(src)
        s=s[:index]+s[index+2:]
    else:
        break
print("Number of times bob occurs is: %d"%cnt)