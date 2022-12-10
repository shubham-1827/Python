#for loops are used to repeate a section of code multiple times.
#syntax:
#	for item in list_of_items:
		#do some work, for every item..

#Range() functions is used when you are using for loops not with the lists.
#syntax:
#	range(start, end, steps) (end is not included in range)

#	for num in range(a, b, c):
		#do some work for every num...

names = ["Shubham", "Adi", "Anjali"]
for name in names:
    print(name)
print(names) #this print is outside for loop

total = 0
for num in range(1, 101):
    total += num #sum of first 100 natural numbers.
print(total)