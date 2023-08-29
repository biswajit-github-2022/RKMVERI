import random
l=[]
for i in range(0,10):
    x= random.randint(1,20)
    l.append(x)
print(l)

min=1100000
for i in range(len(l)):
    if min>l[i]:
        min=l[i]
print(f'Least val: {min}')