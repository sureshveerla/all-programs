import math
N=int(input("Enter No.of Students : "))
R=int(input("Enter No.of Seats : "))
numerator=math.factorial(N)
denominator=math.factorial(N-R)
no_of_ways=numerator//denominator
print('no.of ways to be seated '+str(no_of_ways))
