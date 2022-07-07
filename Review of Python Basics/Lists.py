# Lists - Sequence of values. It can be used to store any type and number of variable and info. Value in list are called elements.
# lists are mutable unlike string and tuples

x = [1,2,3,4,5,6,7,8,9,10,11,12]

# List Comprhension - Elegant and conscise way of creating a new list from and existing list.

x = [i*2 for i in range(10) if(i%2 == 0)]
print(x)

# This equates to

for i in range(10):
    if(i%2==0):
        print(i*2)

# Slicing - Used to create a subset of list using index

print(x[5:])
print(x[:5])
print(x[3:7])
print(x[2:8:2])
print(x[-3:-8])

## Built in list function and methods are -:
# len()
# max()
# min()
# list()
# sum()
# append(item)
# insert(index,item)
# sort()
# reverse()

# Copying list

list1 = [1,2,3]
list2 = list1

# This doesnt make copy of the list. This makes list2 refer the values of list1. So any change in list1 reflects in list2 as well.
# To make copy of list use copy() function

new_list = list1.copy()