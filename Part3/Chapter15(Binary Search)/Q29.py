N, C = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
start = arr[1] - arr[0]
end = arr[len(arr) - 1] - arr[0]
while start >= end:
    mid = (start + end) // 2
    cnt = 1
    value = arr[0]
    for i in range(1, N):
        if arr[i] >= value + mid:
            cnt += 1
            value = arr[i]
    if cnt >= C:
        start = mid + 1
        result = mid
    else:
        end - 1
print(result)