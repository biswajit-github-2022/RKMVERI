l=[1,2,3,4,5,6]
l_1=[]
for i in range(1,len(l)+1):
    l_1.append(l[-i])
print(l_1)

l2=l[-1::-1]
print(l2)