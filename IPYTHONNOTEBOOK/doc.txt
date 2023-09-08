alp=['a','b','c','d']
l1,l2,l3=[],[],[]

for  i in alp:
    for j in alp:
        l1.append(i+j)
        for k in alp:
            l2.append(i+j+k)
            for l in alp:
                l3.append(i+j+k+l)
print(f'number of words = {len(l1)} and words are: {l1}\n')
print(f'number of words = {len(l2)} and words are: {l2}\n')
print(f'number of words = {len(l3)} and words are: {l3}\n')