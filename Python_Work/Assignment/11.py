citywdis={(1,2):10,(1,5):100,(1,4):30,(2,3):50,(3,5):10,(4,3):20,(4,5):60}
l=list(citywdis.keys())
print(l)
res=[]
for i in l:
    if i[0]==1 and i[1]==5:
        res.append((i, citywdis[i]))
        #l.remove(i)
    else:
        for j in l:
            if i[0]==1 and i[1]==j[0]  and j[1]==5:
                res.append((i, j, citywdis[i] + citywdis[j]))
            else:
                for k in l:
                    if i[0] == 1 and i[1] == j[0] and j[1]!=i[0] and j[1] == k[0] and k[1]==5:
                        res.append((i,j,k, citywdis[i] + citywdis[j]+citywdis[k])) 
                    else:
                        for m in l:
                            if i[0] == 1 and i[1] == j[0] and j[1]!=i[0] and j[1] == k[0] and  k[1]!=j[0] and k[1] == m[0] and m[1]==5:
                                res.append((i, j, k,m, citywdis[i] + citywdis[j] + citywdis[k]+citywdis[m]))

print("All possible route",res)
e=[]
for i in res:
    e.append(i[-1])
for i in res:
    if i[-1]==min(e):
        print("shortest route",i[:-1],"\ndistance",min(e))
        break