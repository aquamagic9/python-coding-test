size = int(input())
numberOfApple = int(input())
appleLocation = []
array = [[0] * size for _ in range(size)]
for i in range(numberOfApple):
    value = list(map(int, input().split()))
    value[0] -= 1
    value[1] -= 1
    array[value[0]][value[1]] = 2
    appleLocation.append(value)

numberOfRotation = int(input())
rotationInform = []
for i in range(numberOfRotation):
    rotationInform.append(list(input().split()))
time = 0
tail_time = 0
tail = [0, 0]
tail_dx = 1
tail_dy = 0
j = 0
head = [0, 0]
head_dx = 1
head_dy = 0
i = 0

def rotation(dy, dx, k):
    if rotationInform[k][1] == 'L':
        if dy == 1 or dy == -1:
            dx, dy = dy, dx
        else:
            dx, dy = -dy, dx
    if rotationInform[k][1] == 'D':
        if dx == 1 or dx == -1:
            dx, dy = dy, dx
        else:
            dx, dy = -dy, dx
    return dy, dx


while True:
    print(head[0], head[1])
    if array[head[0]][head[1]] == 2:
        array[head[0]][head[1]] = 1
        head[0] += head_dy
        head[1] += head_dx
        time += 1
        if i < len(rotationInform) and time == int(rotationInform[i][0]):
            head_dy, head_dx = rotation(head_dy, head_dx, i)
            i += 1
        if head[0] < 0 or head[1] < 0 or head[0] >= size or head[1] >= size or array[head[0]][head[1]] == 1:
            break
    else:
        array[head[0]][head[1]] = 1
        head[0] += head_dy
        head[1] += head_dx
        time += 1
        if i < len(rotationInform) and time == int(rotationInform[i][0]):
            head_dy, head_dx = rotation(head_dy, head_dx, i)
            i += 1
        if head[0] < 0 or head[1] < 0 or head[0] >= size or head[1] >= size or array[head[0]][head[1]] == 1:
            break
        array[tail[0]][tail[1]] = 0
        tail[0] += tail_dy
        tail[1] += tail_dx
        tail_time += 1
        if j < len(rotationInform) and tail_time == int(rotationInform[j][0]):
            tail_dy, tail_dx = rotation(tail_dy, tail_dx, j)
            j += 1
print(time)