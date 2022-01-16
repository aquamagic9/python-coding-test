from itertools import combinations

N, M = map(int, input().split())
house = []
chicken = []
for i in range(N):
    row = list(map(int, input().split()))
    for k in range(len(row)):
        if row[k] == 1:
            house.append([k, i])
        elif row[k] == 2:
            chicken.append([k, i])
candidates = list(combinations(chicken, M))

def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for x, y in candidate:
            temp = min(temp, abs(x - hx) + abs(y - hy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
print(result)