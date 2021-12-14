f=None
try:
	f=open("sample.txt","r")
	data=f.read()
	words=data.split()
	l=[]
	for i in words:
		if i.isdigit():
			l.append(i)
	ch=i.split()
	print(l)
	print("number of words = ",len(l))
except FileNotFoundError:
	print("Invalid file name")
finally:
	if f:
		f.close()