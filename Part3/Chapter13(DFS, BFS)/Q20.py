import copy
from itertools import combinations

# 감시
def watch(y, x, dy, dx):
    global new_array
    global N
    global new_students
    while 0 <= y < N and 0 <= x < N:
        if new_array[y][x] == 2:  # S
            new_students.remove((y, x))
            new_array[y][x] = 0
        elif new_array[y][x] == 3 or new_array[y][x] == 1:  # O or T
            return;
        y += dy
        x += dx


N = int(input())
array = [N * [0] for _ in range(N)]
blank = []
teachers = []
students = []
# X:0 T:1 S:2 O:3
for y in range(N):
    row = list(input().split())
    for x in range(len(row)):
        if row[x] == 'X':
            blank.append((y, x))
        elif row[x] == 'T':
            array[y][x] = 1  # T
            teachers.append((y, x))
        elif row[x] == 'S':
            array[y][x] = 2
            students.append((y, x))

result = 'NO'
# 장애물 3자리 경우의 수
for picks in combinations(blank, 3):
    new_array = copy.deepcopy(array)
    for py, px in picks:
        new_array[py][px] = 3  # O
    new_students = copy.deepcopy(students)
    # 감시 범위 탐색
    for ty, tx in teachers:
        watch(ty - 1, tx, -1, 0)
        watch(ty + 1, tx, 1, 0)
        watch(ty, tx + 1, 0, 1)
        watch(ty, tx - 1, 0, -1)
    # 모든 학생이 감시 범위에서 벗어나 있다면
    if len(new_students) == len(students):
        result = 'YES'
        break
print(result)
