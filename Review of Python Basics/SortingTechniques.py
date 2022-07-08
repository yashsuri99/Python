# Bubble Sort - List traversed by comparing its adjacent elements, sorting them and swapping the lists.

x = [3,2,4,1]

for i in range(len(x)-1):
    for j in range(len(x)-i-1):
        if(x[j]>x[j+1]):
            x[j],x[j+1] = x[j+1],x[j]

print(x)
# Insertion Sort

x = [2,3,2,3,5]

for i in x:
    j = x.index(i)
    while(j>0):
        if(x[j-1] > x[j]):
            x[j-1],x[j] = x[j],x[j-1]
        else:
            break
        j = j-1

print(x)