#if statement is a statement that only executes if the given condition is true.
#if condition is false, then, else statement executes.
#you can use elif (else if) to check for multiple conditions in same control flow.
# syntax:
#	if condition1:
		#do this...
#	elif condition2:
		#do that....
#	else:
		#do something else....

#you can also nest if else statements, means 1 if statement ke andar aur if statements.

#multiple if statements are used if you want to check multiple conditions in different 
#control flows at the same indentation label.
#like:
#	if condition1:
		#do A
#	if condition2:
		#do B
#if both the statements are true, both if statements will execute.

#logical operators:
	#and, or, not
#and - gives true if both conditions are true.
#or - gives false only if both conditions are false.
#not - reverses the boolean value (like if a is true, not(a) is false)

print("Welcome to the Roller Coaster Ride!!\n")
height = int(input("What is your height(in cm)? "))

if height>=120:
    print("You are eligible for the Ride!!")

    age = int(input("Please enter your age? "))
    bill = 0

    if age<12:
        bill = 5
        print("Your total bill is $5")
    elif age<=18:
    	bill = 10
    	print("Your total bill is $10")
    elif age>=45 and age<=55:
        print("Everything will be okay, enjoy the free ride from our side!!")
    else:
        bill = 12
        print("Your total bill is $12")
    
    want_photos = input("Do you want to take photos? (Y/N) : ")
    if want_photos == "Y" or "y":
        bill+=3
        print("Taking photos will charge $3 extra")

    print(f"Your total Bill is ${bill}")
else:
    print("Sorry Bro, grow taller and come back!!")


		