#functions in python are used to split the code into multiple blocks of code.
#using functions help to modularize the code and inprove readability.
#syntax:
#Defining a function:

#	def func_name():
#		do this...
#		then do this...
#		finally do this...

#calling a finction:
#you can only call a function to use it after defining it.
# func_name()

#nothing inside this function will execute until the function is called.
def my_function():
    print("Hello")
    print("Bye")

#calling
my_function()

#functions with inputs:
	#syntax:
    #fnction_name(input1, input2,.....)

    #calling:
    #function_name(12, 14, 15, .....)
    #(so, input1 = 12, input2 = 14 and so on...)

#the things wriitten inside the parentheses during the declaration are called parameters.
def greet(name, location):
    print(f"Hello {name}.")
    print(f"What's the weather in {location}?")

##the things wriitten inside the parentheses during the calling of function are called arguments.
#calling the function with positional arguments (means you need to give the arguments 
#in same order as the parameters.)
greet("Shubham", "Harda")

#calling function with the keyword arguments (now, order of arument has no importance)
greet(location="Harda", name="Adi")
