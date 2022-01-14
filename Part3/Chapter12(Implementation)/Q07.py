N = int(input())

left = str(N)[:len(str(N))//2]
right = str(N)[len(str(N))//2:]

sum = 0
for i in range(len(left)):
    sum += int(left[i])
    sum -= int(right[i])
if sum == 0:
    print('LUCKY')
else:
    print('READY')
