from collections import deque
# N x N 크기의 땅, L명 이상 R명 이하 일 때 인구 이동
N, L, R = list(map(int, input().split()))
array = [N * [0] for _ in range(N)]
for y in range(N):
    row = list(map(int, input().split()))
    for x in range(len(row)):
        array[y][x] = row[x]
packet = []
queue = deque()
result = 0
while True:
    flag = 1
    visit_array = [N * [0] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if visit_array[y][x] == 0:
                queue.append((y, x))
                packet.append((y, x))
                visit_array[y][x] = 1
            repeat_check = 0
            while queue:
                repeat_check += 1
                py, px = queue.popleft()
                if py - 1 >= 0 and visit_array[py - 1][px] == 0 and L <= abs(array[py - 1][px] - array[py][px]) <= R:
                    queue.append((py - 1, px))
                    packet.append((py - 1, px))
                    visit_array[py - 1][px] = 1
                if py + 1 < N and visit_array[py + 1][px] == 0 and L <= abs(array[py + 1][px] - array[py][px]) <= R:
                    queue.append((py + 1, px))
                    packet.append((py + 1, px))
                    visit_array[py + 1][px] = 1
                if px - 1 >= 0 and visit_array[py][px - 1] == 0 and L <= abs(array[py][px - 1] - array[py][px]) <= R:
                    queue.append((py, px - 1))
                    packet.append((py, px - 1))
                    visit_array[py][px - 1] = 1
                if px + 1 < N and visit_array[py][px + 1] == 0 and L <= abs(array[py][px + 1] - array[py][px]) <= R:
                    queue.append((py, px + 1))
                    packet.append((py, px + 1))
                    visit_array[py][px + 1] = 1
            if repeat_check > 1:
                flag = 0
                sum_packet = 0
                for ty, tx in packet:
                    sum_packet += array[ty][tx]
                avg = sum_packet // len(packet)
                for ty, tx in packet:
                    array[ty][tx] = avg
            packet = []
    if flag == 1:
        print(result)
        break
    else:
        result += 1

#방문 했을때 방문처리를 바로 해주지않아 똑같은 좌표가 큐에 추가되는 오류가 있었음