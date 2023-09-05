import random
l=[]
for i in range(0,10):
    x= random.randint(1,20)
    l.append(x)
print(l)
length=len(l)

i=0
while i<length:
    j=i+1
    while j<length:
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
            i=-1
        else :
            j+=1
    i+=1
print(l)