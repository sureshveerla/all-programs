def fact(n):
	if(n==1):
		return 1
	else:
		return n*fact(n-1)
if __name__=='__main__':
	n=int(input("Enter any Number : "))
	res=fact(n)
	print("factorial =",res)

