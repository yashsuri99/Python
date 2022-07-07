# String - String is sequence of characters that may contain letter, number and special characters enclosed within single or double 
# quote. Single character is accessed using index. They are immutable.

# String Operations - Concatenation(+), Repition(*), Membership(in/not in), Range(start,stop,[step]), Slice[n:m]

x = 'Hello'
y = 'World'

z = x + y
print(z)

print(x*3)

print('H' in x)

print('h' not in x)

a = x[2:4]
print(a)

# Traversing String - Means accessing all the elements of the string on after the other using index value.

var = "Hello World"

print(var[1])
print(var[3])
print(var[7])

# Traversing using loop

for i in var:
    print(i)

# Traversing using loop and range

for i in range(0,len(var)):
    print(var[i])

# String Slicing - Retrieves a substring from a string 

z = var[1:8:1]
x = var[1:8:2]
y = var[1:8]

## Other built in string methods are-:
# isalpha()
# isdigit()
# len()
# split()
# lower()
# islower()
# upper()
# isupper()
# replace()
# lstrip()
# rstrip()
# join()
# swapcase()
# ord()
# ch()