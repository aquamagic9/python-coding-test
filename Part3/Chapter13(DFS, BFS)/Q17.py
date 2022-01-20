N, K = map(int, input().split())
array = [N * [0] for _ in range(N)]
virus = []
for y in range(N):
    row = list(map(int, input().split()))
    for x in range(len(row)):
        if row[x] != 0:
            array[y][x] = row[x]
            virus.append((y, x, row[x]))
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