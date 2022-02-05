import sys
input = sys.stdin.readline
T = int(input())
result = []
for _ in range(T):
    N = int(input())
    result = []
    new_recruits = []
    for _ in range(N):
        t1, t2 = map(int, input().split())
        new_recruits.append((t1, t2))
    new_recruits.sort(key=lambda x:x[0])
    min = new_recruits[0][1]
    cnt = 1
    for test1, test2 in new_recruits:
        if test2 < min:
            cnt += 1
            min = test2
    print(cnt)
