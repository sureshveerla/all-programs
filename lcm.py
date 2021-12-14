n1=int(input("Enter First Number : "))
n2=int(input("Enter Second Number : "))
def lcmfinder(n1,n2):
	if(n1>n2):
		larger=n2
	else:
		larger=n1
		while(True):
			if((larger%n1==0) and (larger%n2==0)):
				lcm=larger
				break
			larger=larger+1
		print("Lcm of given Numbers is : ",lcm)
lcmfinder(n1,n2)

