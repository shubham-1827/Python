# print("hello " + 12) 
# this will give you the error as you cant concatenate a string with integer.

#you can check for datatypes by using the type function.
print(type("Hello"))
print(type(67))

a = 12.43
print(type(a))

b = False
print(type(b))

print("\n")

#you can also convert the data types.

#now you can concatenate as both are strings now.
print("Hello " + str(12))
print(str(70) + str(80))
print(70 + float(80))

#print(70 + str(80))
#this will produce error because 70 is integer and 80 is converted to string.