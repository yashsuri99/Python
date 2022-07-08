# Dictionary - Items in a dictionary are present in key-value pairs. The key is immutable but the values are mutable.

dict = {1:'Physics', 2:'Chemisty', 3:'Maths', 4:'English'}

# Iterating through a dictionary

for i in dict:
    print(dict[i])

for key,value in dict.items():
    print(key,value)

# Updating Elements

dict[4] = 'Computer Science'
dict[5] = 'English'

for key,value in dict.items():
    print(key,value)

# Dictionary function are 
# items()
# keys()
# values()