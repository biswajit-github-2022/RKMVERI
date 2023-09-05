l=[7, 4, 1, 17, 19, 17, 1, 5, 3, 10]
# l=list(set(l))
# print(l)
for i in range (0,len(l)):
    for j in range(i+1,len(l)):
        if (l[i]*l[j])%2!=0 :
            print(f'({l[i]}, {l[j]})')
