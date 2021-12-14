try:
	a=int(input("Enter First Number "))
	b=int(input("Enter Second Number "))
	c=a/b
	print("c =",c)
	l=[10,20,30]
	print(l[3])
except ZeroDivisionError:
	print("second number should not be Zero ")
except ValueError:
	print("Enter digits only ")
except IndexError:
 	print("Invalid list index")
except Exception:
	print("error")
print("hello")	