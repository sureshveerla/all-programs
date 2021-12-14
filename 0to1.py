n=int(input("Enter Any Number :"))
r=str(n)
n=list(r)
for i in range(len(n)):
	if(n[i]=='0'):
		n[i]='1'
		r=r+n[i]
del n
print(int(r))