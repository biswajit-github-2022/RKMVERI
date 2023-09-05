import sys
l=l=[2, 10, 15, 16, 8, 11, 8, 1, 15, 10]
l1=[]
length=len(l)
c=0
while len(l)>0:
    min=sys.maxsize
    for i in range(length-c):
        if min>l[i]:
            min=l[i]
    l1.append(min)
    l.remove(min)
    c+=1

# print(l1)
# l=[1,2,3,4,5]
# l.remove(1)
# print(l)


# l=[5,3,54,3,5,68,55]
# sorted_l=[]
# for i in l:
#     min=l[0]
#     for number in l:
#         if min>number:
#             min=number 
#             print(min)
#     sorted_l.append(min)
#     l.remove(min)
# print(sorted_l)

# l1=[9,8,7,6]
# l1.remove(8)
# for i in l1:
#     print(i)

# 