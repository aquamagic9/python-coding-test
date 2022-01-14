def current_food():
    food_times = list(map(int, input().split()))
    k = int(input())
    result = -1
    cnt = 0
    while True:
        zero_cnt = 0
        for i in range(len(food_times)):
            if food_times[i] == 0:
                zero_cnt += 1
                continue
            if k == cnt:
                result = i
                return result
            food_times[i] -= 1
            cnt += 1
        if zero_cnt == len(food_times):
            return result


print(current_food() if current_food() != -1 else -1)
