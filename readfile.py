f=None
try:
	f=open("sample.txt","r")
	data=f.read()
	ch=[]
	for i in data:
		if i.isdigit():
			ch.append(i)
	print("number of characters = ",len(ch))
except FileNotFoundError:
	print("Invalid file name")
finally:
	if f:
		f.close()