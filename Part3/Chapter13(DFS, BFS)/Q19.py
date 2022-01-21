from itertools import permutations

# 사칙연산 리스트로 만들기
def make_list(a, b):
    list = []
    for i in range(len(a) - 1):
        list.append(str(a[i]))
        list.append(b[i])
    list.append(str(a[len(a) - 1]))
    return list

# 사칙 연산 순서대로 수행(우선 순위 고려 X)
def calculate_list(list):
    result = int(list[0])
    for i in range(1, len(list), 2):
        if list[i] == '+':
            result = result + int(list[i + 1])
        elif list[i] == '-':
            result = result - int(list[i + 1])
        elif list[i] == '*':
            result = result * int(list[i + 1])
        elif list[i] == '/':
            # 음수 나눗셈은 C++14를 따른다
            if result < 0:
                result = -(-result // int(list[i + 1]))
            else:
                result = result // int(list[i + 1])
    return result

N = int(input())
result = []
num_list = list(map(int, input().split()))
calculate = list(map(int, input().split()))
sign = ['+', '-', '*', '/']
cal = []
for i in range(len(calculate)):
    for _ in range(calculate[i]):
        cal.append(sign[i])
# 완전 탐색
for case in permutations(cal, len(cal)):
    list = make_list(num_list, case)
    result.append(calculate_list(list))
print(max(result))
print(min(result))