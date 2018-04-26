def McNuggets(n):
    """
    n is an int
    6a+9b+20c=n
    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    flag=False
    for i in range(n//6+1):
        for j in range(n//9+1):
            for k in range(n//20+1):
                if 6*i+9*j+k*20==n:
                    flag=True
                    break
    return flag
print(McNuggets(6))
print(McNuggets(9))
print(McNuggets(15))
print(McNuggets(20))
print(McNuggets(26))
print(McNuggets(29))
print(McNuggets(12))
print(McNuggets(27))
print(McNuggets(40))
print(McNuggets(21))
