try:
	a=int(input("Enter Any Number = "))
	b=int(input("Enter Any Number = "))
	c=a/b
	print("c = ",c)
	l=[10,20,30]
	print(l[3])
except ZeroDivisionError:
	print("Second number should not be 0")
except ValueError:
	print("Enter only digits")
except IndexError:
	print("Invalid List index")
except Exception:
	print("error")
print("hello")