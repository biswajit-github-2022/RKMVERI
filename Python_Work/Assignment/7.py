import random
l=[]
for i in range(0,10):
    x= random.randint(1,20)
    l.append(x)
print(l)
length=len(l)

i=0
while length>i:
    for j in range(length-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
    i+=1
print(l)