N = int(input())
won = list(map(int, input().split()))
won.sort()
result = 1
for i in won:
    if result < i:
        break
    else:
        result += i
print(result)
