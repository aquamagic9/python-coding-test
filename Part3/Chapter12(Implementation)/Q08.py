string = input()
stringList = list(string)
stringList.sort()
num = -1
not_num = ''
for i in range(len(stringList)):
    if '0' <= stringList[i] <= '9':
        if num == -1:
            num = 0
        num += int(stringList[i])
    else:
        not_num += stringList[i]
if num == -1:
    print(not_num)
else:
    print(not_num + str(num))