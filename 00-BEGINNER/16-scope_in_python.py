#in python only functions and classes have scopes, 
#unlike other languages, (like c++)
	#block scope for loops (for, while) and conditional statements (if, else) is not there in python.

#means if you define a variable inside the loop or an if statement you can access that variable anywhere in the program,
	#but, if you define it inside a function then that variable is only accessible inside that function.

#the variable defined independent of any function is called a global variable.
#you, cant directly modify a global variable, inside a function.
#to modify it, you need to use the global keyword.
	#let num1 = 3 be global, so
    # my_finc():
    	#global num1
        #num1 = 5

#in python the naming style for declaring constants is all uppercase letters.
#(you can still change these constants but seeing it in all uppercase you will be notified that this is a constant.)
#best practice is to define constants at the top of the program.
PI = 3.14159

num1 = 4

def my_function():
    num1 = 6
    print(f"num1 inside function : {num1}")

my_function()
print(f"num1 outside function : {num1}")

print("\nUsing global keyword!!")

def my_function1():
    global num1
    num1 = 6
    print(f"num1 inside function : {num1}")

my_function1()
print(f"num1 outside function : {num1}")