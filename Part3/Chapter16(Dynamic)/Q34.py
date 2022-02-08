N = int(input())
arr = list(map(int, input().split()))
arr.reverse()
dp = [1] * N
for i in range(len(arr)):
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))
print(dp)
#10
#5 4 10 9 8 7 6 5 4 3 2 1