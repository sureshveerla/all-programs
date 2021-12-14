numbers=[1,4,2,100,20,50,32,200,150,8]
big=0
for num in numbers:
	if(big<num):
		big=num
print("first biggest value = ",big)
big1=0
for num in numbers:
		if(big1<num and num!=big):
			big1=num
print("second biggest value = ",big1)