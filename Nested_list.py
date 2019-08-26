students=[]
score_list=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
    score_list.append(score )
    
second_lowest_mark = sorted(list(dict.fromkeys(score_list)))[1]

for name,score in sorted(students):
    if score == second_lowest_mark:
        print(name)
