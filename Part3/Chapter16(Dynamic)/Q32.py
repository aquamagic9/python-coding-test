N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            left = 0
        else:
            left = arr[i - 1][j - 1]
        if j == i:
            right = 0
        else:
            right = arr[i - 1][j]
        arr[i][j] = arr[i][j] + max(left, right)
result = 0
for j in range(N):
    result = max(result, arr[N - 1][j])
print(result)