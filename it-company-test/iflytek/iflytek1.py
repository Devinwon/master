q='LRRLRL'
cnt=len(q)
while 'RL' in q:
    index=q.index('RL')
    if index>=1 and index < len(q)-2:
        try:
            if q[index-1]=='R' or q[index+2]=='L':
                q=q[:index]+q[index+1:]
            else:
                q=q[:index]+q[index+2:]
            cnt-=1
        except:
            pass
    elif index==0:
        try:
            if len(q)>= 3:
                if q[index+2]=='L':
                    q=q[index+1:]
                else:
                    q=q[index]+q[index+2:]
                
            else:
                q=q[0]
            cnt-=1
        except:
            pass
    elif index==len(q)-2:
        try:
            if len(q)>= 3:
                q=q[:index]+q[-1]
            else:
                
                q=q[0]
            cnt-=1
        except:
            pass

print(cnt)