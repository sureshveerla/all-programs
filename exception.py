class AgeError(Exception):pass
if __name__ =='__main__':
	try:
		eid=int(input("Enter Employee Id : "))
		ename=input("Enter Employee Name : ")
		salary=float(input("Enter Employee Salary : "))
		age=int(input("Enter Employee Age : "))
		if(age<20 or age>40):
			raise AgeError()
		else:
			print("Employee Record Created Successfully ")
			print("Employee id : ",eid)
			print("Employee Name : ",ename)
			print("Employee Salary : ",salary)
			print("Employee Age : ",age)
	except AgeError:
		print("Age should be in between in 20 and 40") 