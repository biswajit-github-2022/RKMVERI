
def inp_file_names():#f1
    a=input("Enter File Name Containing Grade Structure : ")
    b=input("Enter File Name Containing Marks : ")
    return a,b



def process(s1,s2):#f1
    l=[]
    t_l=[]
    gs=open(s1)
    ml=open(s2)
    gs_lines=gs.readlines()
    for i in range(len(gs_lines)):
        gs_lines[i]=gs_lines[i].strip('\n')
        l.append(gs_lines[i].split(':'))
    for i in l:
        for j in range(len(i)-1):
            i[j+1]=int(i[j+1])
        t=tuple(i)
        t_l.append(t)

    ml_line=ml.readline()
    ml_list=[]
    l=ml_line.split(',')
    # print(l[0])
    for i in range(len(l)):
        l[i]=int(l[i])

    return t_l,l



def create_result (p1,p2):
    l_class=[]
    for i in p1:
        l_class.append([])
    x=[]
    grade_box={}
    for i in p2:
        for j in range(len(p1)):
            if i<=p1[j][1] and i>=p1[j][2]:
                l_class[j].append(i)
    for i in range(len(p1)):
        grade_box[p1[i][0]]=l_class[i]
        x.append((p1[i][0],len(l_class[i])))

    return grade_box,tuple(x)


def generate_grade_score():#f3
    file_names = inp_file_names()#f1
    res = process(file_names[0],file_names[1])#f2
    result=create_result(res[0],res[1])#f3
    return result

result=generate_grade_score()
print(result)