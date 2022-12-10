#list:
	#lists are data structures used to store large data.
    #you can store string with numbers floats ... etc.

#syntax:
#	list = [item1, item2, item3, .....]

#you can access any list item by using its index position.
#(index position starts from 0)
#	print(list[1]) - prints 2nd item in list.

#functions in list:
#1 - append:
#	list.append("shubham")
#	it adds a new item at the end of list.

#2 - extend:
#	you can add another list to a list

#3 - pop:
#	removes an item from the end of the list.

list = ["Shubham", "Adi", "Anjali"]
print(list)
print(list[1])
list.append("Ayush")
print(list)
list.extend(["Aditya", "Priyanshu"])
print(list)
list.pop()
print(list)