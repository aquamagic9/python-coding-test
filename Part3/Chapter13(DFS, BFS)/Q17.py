# N:배열의 크기 K:바이러스의 종류
N, K = map(int, input().split())
array = [N * [0] for _ in range(N)]
virus = []
# 배열 입력
for y in range(N):
    row = list(map(int, input().split()))
    for x in range(len(row)):
        if row[x] != 0:
            array[y][x] = row[x]
            virus.append((y, x, row[x]))
# time 후에 py, px 좌표의 바이러스 종류 계산
time, py, px = map(int, input().split())
for i in range(time):
    new_virus = []
    for y, x, num in virus:
        if y - 1 >= 0 and array[y - 1][x] == 0:
            array[y - 1][x] = num
            new_virus.append((y - 1, x, num))
        if y + 1 < N and array[y + 1][x] == 0:
            array[y + 1][x] = num
            new_virus.append((y + 1, x, num))
        if x - 1 >= 0 and array[y][x - 1] == 0:
            array[y][x - 1] = num
            new_virus.append((y, x - 1, num))
        if x + 1 < N and array[y][x + 1] == 0:
            array[y][x + 1] = num
            new_virus.append((y, x + 1, num))
    virus = new_virus
print(array[py - 1][px - 1])