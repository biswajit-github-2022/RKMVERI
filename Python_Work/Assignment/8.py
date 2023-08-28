sentence= "this can't be a problem's solution"
l=list(sentence)
c=l.count('\'')
for i in range(c):
    l.remove("\'")
# print(l)
sentence=''.join(l)
print(sentence)