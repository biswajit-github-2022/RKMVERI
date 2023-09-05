import sys
l=[2, 10, 15, 16, 8, 11, 8, 1, 15, 10]

min=sys.maxsize
for i in range(len(l)):
    if min>l[i]:
        min=l[i]
print(f'Least val: {min}')