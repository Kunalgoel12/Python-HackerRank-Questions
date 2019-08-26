n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()   
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
sum=00.00
for key,value in student_marks.items():
    marks=student_marks.get(query_name)
for i in range(len(marks)):
    sum=sum+marks[i]
    average=sum/len(marks)
print('%.2f' % average)
