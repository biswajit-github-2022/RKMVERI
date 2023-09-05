import random
l=[]
for i in range(0,10):
    x= random.randint(1,20)
    l.append(x)
print(l)
length=len(l)
for i in range(length-1): 
    for j in range(length-i-1): # go the beginning of the sequence
        if l[j]>l[j+1]:     #if left one is more than right one
            l[j],l[j+1]=l[j+1],l[j]  #swap the consecutive values 
print(l)