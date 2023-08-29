import random
l=[]
for i in range(0,10):
    x= random.randint(1,20)
    l.append(x)
print(l)
l=list(set(l))
# print(l)
for i in range (0,len(l)):
    for j in range(i,len(l)):
        if (l[i]*l[j])%2!=0 and l[i]!=l[j]:
            print(f'({l[i]}, {l[j]})')
# print(l)
