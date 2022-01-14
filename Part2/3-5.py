N, M = map(int, input().split())

cnt = 0
while (N != 1):
    if N % M != 0:
        N -= 1
    else:
        N //= M
    cnt += 1
print(cnt)
