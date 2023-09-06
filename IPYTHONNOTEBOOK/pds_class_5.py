marks_list=[]
for i in range(100):
    x=random.randint(1,100)
    marks_list.append(x)
# marks_list

l1=[]
l2=[]
l3=[]
grade_box={"A":[],"B":[],"C":[]}
for i in marks_list:
    if i<=100 and i>=80:
        l1.append(i)
    if i<80 and i>=60:
        l2.append(i)
    if i<60:g
        l3.append(i)

grade_box["A"]=l1
grade_box["B"]=l2
grade_box["C"]=l3

grade_box