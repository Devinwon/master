'''
In:I like beijing.

Out:beijing. like I
'''
words=list(input().split())

print(' '.join(words[::-1]))