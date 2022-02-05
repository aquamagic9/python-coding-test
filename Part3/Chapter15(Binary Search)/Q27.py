def find_left(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target and (mid == 0 or array[mid - 1] < target):
            return mid
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return None
def find_right(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target and (mid + 1 == len(array) or array[mid + 1] > target):
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

N, target = map(int, input().split())
array = list(map(int, input().split()))
left_index = find_left(array, target, 0, len(array) - 1)
right_index = find_right(array, target, 0, len(array) - 1)
if left_index == None:
    print(-1)
else:
    cnt = right_index - left_index + 1
    print(cnt)