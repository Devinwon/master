#-*- coding: UTF-8 -*-
# 闂��绠�堪锛氬亣璁句竴鏀�毊鐞冧粠100绫抽珮搴﹁嚜鐢辫惤涓嬨�鏉′欢锛屾瘡娆¤惤鍦板悗鍙嶈烦鍥炲師楂樺害鐨勪竴鍗婂悗锛屽啀钀戒笅銆�
# 瑕佹眰锛氱畻鍑鸿繖鏀�毊鐞冿紝鍦ㄥ畠鍦ㄧ�10娆¤惤鍦版椂锛屽叡缁忚繃澶氬皯绫筹紵绗�0娆″弽寮瑰�楂橈紵
oriheight=100
fallSn=int(input("璁惧畾涓嬭惤娆℃暟锛�))
# 鐞冪�n娆′笅钀藉悗鍙嶅脊鐨勯珮搴�
def ballHeight(n):
    return oriheight*1/(2**n)

def distance(m):
    s=0.0
    for i in range(1,m+1):
        s+=1/(2**(i-1))
    s=s*oriheight
    return s

print("绗�,fallSn,"娆¤惤鍦版椂鍏辩粡杩�",distance(fallSn),"绫�)
print("绗�,fallSn,"娆¤惤鍦板悗鍙嶅脊",ballHeight(fallSn),"绫�)
