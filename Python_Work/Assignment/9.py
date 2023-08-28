alp=['a','b','c','d']
c=0
Word=[]
for  i in range(len(alp)):
    for j in range(len(alp)):
        c+=1
        word=alp[i]+alp[j]
        Word.append(word)
print(f'number of words = {c} and words are: {Word}\n')

c=0
Word=[]
for  i in range(len(alp)):
    for j in range(len(alp)):
        for k in range(len(alp)):
            c+=1
            word=alp[i]+alp[j]+alp[k]
            Word.append(word)
print(f'number of words = {c} and words are: {Word}\n')

c=0
Word=[]
for  i in range(len(alp)):
    for j in range(len(alp)):
        for k in range(len(alp)):
            for l in range(len(alp)):
                c+=1
                word=alp[i]+alp[j]+alp[k]+alp[l]
                Word.append(word)
print(f'number of words = {c} and words are: {Word}\n')