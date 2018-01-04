

def writeTotxt(src_list):
	with open("userdata.txt",'w') as f:
		f.write("info of users are winners \n")
		for v in src_list:
			f.write(str(v)+'\n')
