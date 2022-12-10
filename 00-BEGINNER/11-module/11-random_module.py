#module:
#	modules are divisions of code.
#	of you have a very large program you mibght want to divide that program into 
#different subsections sp these subsections are called as modules.

#pyrhon provides some precreated modules loke random module, but you can also create 
#your own modules, and add them to your main.py by using import.

import random
import my_module

random_number = random.randint(1, 100)
print(random_number)

random_float = random.random() #generates floating pointing number in range [0,1)
print(random_float)

random_float1 = random_float*5 #generates float in range [0,5)
print(random_float1
)
value_of_pi = my_module.pi
print(value_of_pi)
