Month=int(input("Enter Month : "))
Year=int(input("Enter Year : "))
if(Month == 2 and (Year%400 == 0) or ((Year%100 != 0) and (Year%4 == 0))):
	print("Number of Days is 29 days")
elif(Month==2):
	print("Number of Days is 28 days")
elif(Month==1 or Month==3 or Month==5 or Month==7 or Month==8 or Month==10 or Month==12):
	print("Number of Days is 31 days")
else:
	print("Number of Days is 30 days") 