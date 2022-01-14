N = int(input())

direction = input().split()
x,y = 1, 1
for i in range(len(direction)):
    if direction[i] == 'R' and x + 1 < N:
        x += 1
    elif direction[i] == 'L' and x - 1 > 0:
        x -= 1
    elif direction[i] == 'U' and y - 1 > 0:
        y -= 1
    elif direction[i] == 'D' and y + 1 < N:
        y += 1
print(y, x)