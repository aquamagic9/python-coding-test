N = int(input())
houses = list(map(int, input().split()))
houses.sort(reverse=True)
# 내림차순으로 정렬 후 인덱스 // 2 위치의 값
print(houses[N//2])