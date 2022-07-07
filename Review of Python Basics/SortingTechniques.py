# Bubble Sort - List traversed by comparing its adjacent elements, sorting them and swapping the lists.

x = [3,2,4,1]

for i in range(len(x)):
    for j in range(len()-i):
        if(x[j]>x[j+1]):
            x[j],x[j+1] = x[j+1],x[j]

# Insertion Sort

for i in x:
    j = x.index(i)
    while(j>0):
        if(x[j-1] > x[j]):
            x[j-1],x[j] = x[j],x[j-1]
        else:
            break
        j = j-1
