# 一只小猴子第一天摘下若干个桃子，并吃了一半，感觉吃的不过瘾又多吃了一个；
# 第二天又将剩下的桃子吃掉一半，又多吃了一个
# 以后每天早上都吃前一天剩下的一半零一个
# 到了第10天早上再想吃时发现只剩下一个，原先一共又多少桃子？
total=1
for i in range(1,10):
    total=(total+1)*2
print("There are %d peaches in day one" %total)
