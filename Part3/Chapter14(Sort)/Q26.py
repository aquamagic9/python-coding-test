# A + B 번 비교가 아니라 A + B - 1번 비교가 아닌가??
N = int(input())
card = []
for _ in range(N):
    card.append(int(input()))
result = 0
# 카드 리스트에서 가장 작은 값 2개를 뽑아 더한 후 리스트에 다시 추가
while len(card) != 1:
    card.sort()
    result += card[0] + card[1]
    card.append(card.pop() + card.pop())
print(result)