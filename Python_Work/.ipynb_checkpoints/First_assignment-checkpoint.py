List=[10,11,9,2,1,7]
z=0
i=0
length=len(List)
while(i<length):
    next_val=List[i]
    z +=next_val*(i+1)
    i+=1
print(z)