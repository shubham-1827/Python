#dictionaries are also like list, but you have a perticular key associated with a value
#syntax:
	#dictionary = {key1: value1, key2: value2, .....}

name_dictionary = {
    "Shubham": "He is a python developer and a competitive programmer.",
    "Adi": "He is recently studying for NEET.",
    "Anjali": "She is in class 11th, styding for NEET as well."
}

#accessibg an element from a dictionary
print(name_dictionary["Shubham"])

#Adding element to a dictionary.
name_dictionary["Ayush"] = "I dont know what he is doing.."
print(name_dictionary)

#editing element in dicitionary.
name_dictionary["Ayush"] = "I think he is a commerce student, preparing for CA."
print(name_dictionary)

#you can also create an empty dictionary.
empty_dictionary = {}
print(empty_dictionary)

#you can also wipe out the existing dictionary,
#name_dictionary = {}

#looping in dictionary
for key in name_dictionary:
    print(key)
    print(name_dictionary[key])
    print("\n")