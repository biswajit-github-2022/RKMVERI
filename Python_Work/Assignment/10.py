currency=[2000,500,200,100,50,20,10,5,2,1]
l={}
val=1613
for money in currency:
    if val//money>0:
        l[money]=val//money
        val=val%money
print(l)
