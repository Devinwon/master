"""
现在有如下函数

def compare(a, b):
  return a > b

请你在不修改函数的基础上,打印出函数的调用时间
"""

import datetime
def prtTime(f):
	def dec(*args, **kwargs):
		print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
		f(*args, **kwargs)
	return dec

@prtTime
def compare(a, b):
  return a>b

