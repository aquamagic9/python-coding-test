N = int(input())
students = []
# 이름, 국어, 수학, 영어 입력
for i in range(N):
    students.append(list(input().split()))
# 최우선순 => 국어내림차순, 영어오름차순, 수학내림차순, 이름 사전순
students.sort(key=lambda x: (-(int(x[1])), (int(x[2])), -(int(x[3])), x[0]))
for i in range(N):
    print(students[i][0])