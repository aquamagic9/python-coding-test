# N:전체 스테이지 수
N = int(input())
stages = list(map(int, input().split()))
stages.sort()
fails = []
total_cnt = len(stages)
stage_cnt = 0
i = 0
n = 1
# 각 스테이지마다 실패율 구하기
while n != N + 1:
    while i < N and n == stages[i]:
        stage_cnt += 1
        i += 1
    fails.append((n, stage_cnt/total_cnt))
    total_cnt -= stage_cnt
    stage_cnt = 0
    n += 1
# 실패율을 담은 리스트 실패율내림차순으로 정렬 후 스테이지 오름차순 정렬
fails.sort(key=lambda x: (-x[1], x[0]))
for fail in fails:
    print(fail[0])