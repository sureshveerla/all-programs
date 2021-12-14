def show(*suresh,**kumar):
	for val in suresh:
		print(val,end=",")
	print()
	for k,v in kumar.items():
		print(k,":",v)
	print()
if __name__ =='__main__':
	show(10,20,30)
	show("c","c++","java","python","database")
	show(eid=101,ename="rajesh",sal=10000.789)
	show(5,6,7,8,9,eid=101,ename="kumar",sal=10000.789)