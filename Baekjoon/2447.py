num = int(input())
arr = [num * [0] for _ in range(num)]


def recursion(N, start_i, start_j):
    if N == 1:
        return
    n = N // 3
    for y in range(n, 2*n):
        for x in range(n, 2*n):
            arr[start_i + y][start_j + x] = 1
    for y in range(3):
        for x in range(3):
            if not (y == 1 and x == 1):
                recursion(n, start_i + n * y, start_j + n * x)


recursion(num, 0, 0)
for i in range(num):
    for j in range(num):
        if arr[i][j] == 1:
            print(' ',end='')
        else:
            print('*',end='')
    print()