N, M = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
cnt = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] != a[j]:
            cnt += len(a) - j
            break
print(cnt)
