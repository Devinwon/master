"""
check input

0,1 0,3;
可以对其分割后的每项单独进行检查
只要满足一项就为真，我们需要全部满足
"""
import re

cmd=input()
def connCheck(conn):
	reg=r"(\d+,\d+ \d+,\d+;)+"
	com=re.compile(reg)
	rel=re.findall(com,conn)
	if rel:
		return True
	else:
		return False

if not connCheck(cmd):
	print("Invalid format error")
else:
	print("Valid Format ")



