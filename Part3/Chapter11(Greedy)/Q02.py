N = input()
for i in range(len(N)):
    if (i == 0):
        result = int(N[0])
        continue
    if (N[i] == '0' or N[i] == '1' or result == 0 or result == 1):
        result += int(N[i])
    else:
        result *= int(N[i])
print(result)