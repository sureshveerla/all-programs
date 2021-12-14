f1_numerator=int(input('Enter the Numerator of the 1st fraction :'))
f1_denominator=int(input('Enter the Denominatortor of the 1st fraction :'))
f2_numerator=int(input('Enter the Numerator of the 2nd fraction :'))
f2_denominator=int(input('Enter the Denominatortor of the 2nd fraction :'))
if(f1_denominator==f2_denominator):
	Fraction=f1_numerator+f2_numerator
	print('Addition of two fractions are :' + str(Fraction) + '/' + str(f1_denominator))
else:
	Fraction=(f1_numerator*f2_denominator)+(f2_numerator*f1_denominator)
	print('Addition of two fractions are :' +str(Fraction) + '/' +str(f1_denominator*f2_denominator))