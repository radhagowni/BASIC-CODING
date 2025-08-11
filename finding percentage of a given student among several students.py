n=int(input())
student_marks={}
for i in range(n):
    name,*l=input().split()
    scores=list(map(float,l))
    student_marks[name]=scores
query_name=input()
for j in student_marks:
    if j==query_name:
        average=sum(student_marks[j])/3
print("Average marks : {:.2f}".format(average))
