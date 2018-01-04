'''
主程序
'''
from getPrize_excel import lucky_draw
from writetotxt import writeTotxt

prize_item=[["三等奖",3],["二等奖",2],["一等奖",1]]
lucky_dog=[]

lucky_draw(prize_item,"user.xls",lucky_dog)
writeTotxt(lucky_dog)


			



				