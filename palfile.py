f=None
try:
	f=open("sample.txt","r")
	data=f.read()
	s={}
	for i in data:
		s[i]=data.count(i)
		print(s)
except FileNotFoundError:
	print("Invalid File Name")
finally:
	if f:
		f.close()