N = int(input())
T = []
P = []
dp = [0] * N

def find_max(dp, start, end):
    max_value = dp[start]
    for j in range(start + 1, end):
        max_value = max(max_value, dp[j])
    return max_value


for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
#dp[i]는 dp[i + T[i]]이후의 최대값 + 현재값
for i in range(N - 1, -1, -1):
    #dp[i + T[i]]이후의 최대값 + 현재인덱스의 이익량
    if i + T[i] < N:
        max_value = find_max(dp, i + T[i], N)
        dp[i] = P[i] + max_value
    #만약 현재 인덱스의 상담시간이 마지막타임이면
    elif i + T[i] == N:
        dp[i] = P[i]
result = find_max(dp, 0, N)
print(result)
