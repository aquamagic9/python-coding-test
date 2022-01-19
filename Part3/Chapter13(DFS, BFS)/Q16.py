from itertools import combinations
import copy

N, M = map(int, input().split())
virus = []
wall = []
blank = []
array = [M * [0] for _ in range(N)]
cnt = 0
for y in range(N):
    row = list(map(int, input().split()))
    for x in range(M):
        if row[x] == 1:
            wall.append((y, x))
            array[y][x] = 1
        elif row[x] == 2:
            virus.append((y, x))
            array[y][x] = 2
        elif row[x] == 0:
            cnt += 1
            blank.append((y, x))
#blank에서 3개만 뽑아서 flood 돌림
def flood(y, x, cnt, array):
    array[y][x] = 2
    global N
    global M
    if y - 1 >= 0 and array[y - 1][x] == 0:
        cnt -= 1
        cnt = flood(y - 1, x, cnt, array)
    if y + 1 < N  and array[y + 1][x] == 0:
        cnt -= 1
        cnt = flood(y + 1, x, cnt, array)
    if x - 1 >= 0 and array[y][x - 1] == 0:
        cnt -= 1
        cnt = flood(y, x - 1, cnt, array)
    if x + 1 < M  and array[y][x + 1] == 0:
        cnt -= 1
        cnt = flood(y, x + 1, cnt, array)
    return cnt

picks = combinations(blank, 3)
result = []
for pick in picks:
    new_cnt = cnt
    new_array = copy.deepcopy(array)
    for y, x in pick:
        new_array[y][x] = 1
        new_cnt -= 1
    for vy, vx in virus:
        new_cnt = flood(vy, vx, new_cnt, new_array)
    result.append(new_cnt)
print(max(result))