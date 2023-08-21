n=int(input("Enter Number of Elements: "))
i=0
sum=0
while(i<n):
    z=int(input("Enter the number: "))
    sum=sum+z*(i+1)
    i=i+1
print("Sum of the numbers = ",sum)