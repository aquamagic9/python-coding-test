N, M = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

direction = 0


def turn_left(direction):
    direction -= 1
    if (direction < 0):
        direction = 3
    return direction


def turn_back(direction):
    direction -= 2
    if (direction < 0):
        direction += 4
    return direction


cnt = 1
turn_cnt = 0
index_y, index_x, direction = map(int, input().split())
array = []
for i in range(N):
    array.append(list(map(int, input().split())))
d = [[0] * M for _ in range(N)]
d[index_y][index_x] = 1
while True:
    if turn_cnt > 3:
        back_direction = turn_back(direction)
        index_y += dy[back_direction]
        index_x += dx[back_direction]
        if index_y < 0 and index_y >= N:
            break;
        if index_x < 0 and index_x >= M:
            break;
        if array[index_y][index_x] == 1:
            break;
    direction = turn_left(direction)
    next_index_x = index_x + dx[direction]
    next_index_y = index_y + dy[direction]
    if next_index_x < 0 and next_index_x >= M:
        turn_cnt += 1
        continue
    if next_index_y < 0 and next_index_y >= N:
        turn_cnt += 1
        continue
    if array[next_index_y][next_index_x] == 1:
        turn_cnt += 1
        continue
    if d[next_index_y][next_index_x] == 1:
        turn_cnt += 1
        continue
    index_x = next_index_x
    index_y = next_index_y
    turn_cnt = 0
    cnt += 1
    d[index_y][index_x] = 1
print(cnt)