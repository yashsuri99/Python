# Conditional statements are used to perform actions or calculations based on wehter a condition is evaluated as true or false

Age = int(input())

# if statement

if Age >= 18:
    print("Eligible")

# if-else statement

if Age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# if-elif-else statement

if(Age >= 18):
    print("Eligible")
elif(Age < 18):
    print("Not Eligible")
else:
    print("Not Valid")