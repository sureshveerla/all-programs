x=100
def f1():
	x=99
	def f2():
		x=98
		print("inside f2 x value : ",x)
	return(f2)
	print("inside f1 x value : ",x)
def f3():
	print("inside f3 x value : ",x)
if __name__ =='__main__':
	f2=f1()
	f2()