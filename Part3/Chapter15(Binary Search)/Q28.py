def binary(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] >= mid:
            end = mid - 1
        else:
            start = mid + 1
    return None

N = int(input())
array = list(map(int, input().split()))
result = binary(array, 0, len(array) - 1)
if result == None:
    print(-1)
else:
    print(result)