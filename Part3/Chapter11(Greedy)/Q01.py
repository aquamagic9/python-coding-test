N = int(input())
array = list(map(int,input().split()))
array.sort()
array.reverse()
index = 0
cnt = 0
while index < N:
    index += array[index]
    cnt += 1
print(cnt)