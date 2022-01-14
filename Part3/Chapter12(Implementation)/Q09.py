string = input()
length = len(string)
resultList = []
for i in range(length//2, 0, -1):
    index = 0
    cnt = 0
    result = length
    while index + i <= length:
        if string[index : index + i] == string[index + i : index + i + i]:
            cnt += 1
        elif cnt != 0:
            result = result + len(str(cnt)) - i * cnt
            cnt = 0
        index += i
    resultList.append(result)
print(resultList)
print(min(resultList))