N = int(input())
for _ in range(N):
    row, col = map(int, input().split())
    arr = list(map(int, input().split()))
    k = 0
    for i in range(row):
        for j in range(col):
            arr[i].append(arr[k])
            k += 1
    for j in range(1, col):
        for i in range(row):
            if i == 0:
                left_up = 0
            else:
                left_up = arr[i - 1][j - 1]
            if i == row - 1:
                left_down = 0
            else:
                left_down = arr[i + 1][j - 1]
            left = arr[i][j - 1]
            arr[i][j] = arr[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(row):
        result = max(result, arr[i][col - 1])
    print(result)