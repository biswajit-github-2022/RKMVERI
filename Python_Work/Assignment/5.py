import random
l=[]
l1=[]
for i in range(0,10):
    x= random.randint(1,20)
    l.append(x)
print(l)
length=len(l)

c=0
while len(l)>0:
    min=100000
    for i in range(length-c):
        if min>l[i]:
            min=l[i]
    l1.append(min)
    l.remove(min)
    c+=1

print(l1)
# l=[1,2,3,4,5]
# l.remove(1)
# print(l)