students=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
    
for i in range(0,len(students)-1):
    for i in range(0,len(students)-1):
        if students[i][1]>students[i+1][1]:
            temp = students[i][0]
            temp1 = students[i][1]
            students[i][0] = students[i+1][0]
            students[i][1]=students[i+1][1]
            students[i+1][0] = temp
            students[i+1][1] = temp1
tp=[]
x=students[0][1]
for i in range(0,len(students)):
    if students[i][1]>x:
        y=students[i][1]
        break;
for i in range(0,len(students)):
    if students[i][1]==y:
        tp.append([students[i][0],students[i][1]])
tp.sort()
for i in range(0,len(tp)):
    lt=tp[i][0]
    print(lt)
