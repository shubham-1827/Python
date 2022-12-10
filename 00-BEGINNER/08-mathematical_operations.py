#you can directly do operations with numbers.
print(4 + 3)
print(4 - 3)
print(4 * 3)
print(4 / 3)

#note: division in always gives a float in return even if it is a perfect division
print(4 / 2) # result - 2.0

#you can do operations with variables.
result = (4*3)
print (result)

result = result / 3 #4.0
print (result)

#compound assignment operators.
	#like - +=, -= , *=, /=, ....
a = (5*6)
print (a)

a+=4 #34 (equivalent to a = a + 4)
print(a)

#power operator(**)
print(2**3) # 2 power 3 = 8

#floor operator (//)

print(6 // 4) #gives the integer value of a float.
print(type(6//4))

#round function
	#rounds to nearest integer.
print(round(4/3))
print(round(5/2))

#you can also set presicion in round function
print(round(10/3, 4)) # means upto 4 decimal places