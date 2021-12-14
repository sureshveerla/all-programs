matrix=[]
rows=int(input("Enter No.of Rows "))
columns=int(input("Enter No.of Columns "))
for i in range(0,rows):
	l=[]
	for j in range(0,columns):
		x=int(input("Enter"+str(i+1)+"row"+str(j+1)+"column"))
		l.append(x)
	matrix.append(l)
print(matrix)
#sum of row values
for i in range(0,rows):
	sum=0
	for j in range(0,columns):
		sum=sum+matrix[i][j]
print("row",i+1,"sum",sum)	