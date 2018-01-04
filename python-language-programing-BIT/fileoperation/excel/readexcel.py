'''
将用户输入路径的文件excel打印出来
'''

import xlrd
# path=input('请输入excel文件路径：')
workbook=xlrd.open_workbook("test.xls")

# 第0个表单页,行列结合，遍历单元格

sheet=workbook.sheet_by_index(0)
for row in range(sheet.nrows):
	print()
	for col in range(sheet.ncols):
		print(sheet.cell(row,col).value,"\t",end="")

print()
		
'''
sheet.row(row)[col].value
sheet.col(col)[row].value
sheet.cell(row,col).value
更详细的需要参见相关文档

# 按行遍历，示例结果：
[text:'姓名', text:'性别', text:'地址']
for row in range(sheet.nrows):
	print("%7s"%sheet.row(row))

按列遍历，示例结果
[text:'姓名', text:'李浩', text:'马云', text:'齐天']
for col in range(sheet.ncols):
	print("%7s"%sheet.col(col))

'''

