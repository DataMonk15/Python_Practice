import random


# random numbers are used to generate random numbers in the given range

names_String = "naveen,kumar,fanatics"

list_string = names_String.split(",")
print(list_string)

random_int = random.randint(0,len(list_string)-1)

print(list_string[random_int])
