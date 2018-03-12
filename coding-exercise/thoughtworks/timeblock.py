
'''
check the time block
'''
def check_timeblock(t_str):
    return  int(t_str[6:8])<=22 and int(t_str[:2])>=9 and t_str[3:5]=='00' and t_str[-2:]=='00' and int(t_str[6:8])>int(t_str[:2])

# print(check_timeblock("09:00~19:00"))

