# Tuple - It is a collection of python objects seperated by commas. Tuple is a sequence of immutable python objects.

tup = (1,2,3,4,5)
tup1 = (7,8,9)

for i in tup:
    print(i)

for i in range(0,len(tup)):
    print(tup[i])

# In tuples we can use len(), concatenation(+), repition(*), membership(in/not in), min, max, iteration like above

# Slicing

x = tup[1:4]

tup2 = tup + tup1
print(tup2)