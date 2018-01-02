from time import strftime

# filenamed by date
filenm=strftime("%Y%m%d")
with open(filenm+".txt","a+") as f:
	f.write("123\n")
