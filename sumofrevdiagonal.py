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
#sum of principle of reverse of  Diagonal Elements
sum=0
for i in range(0,rows):
	for j in range(0,columns):
		if(i+j==rows-1):
			sum=sum+matrix[i][j]
print("sum of principal of reverse Diagonal elements",sum)
	