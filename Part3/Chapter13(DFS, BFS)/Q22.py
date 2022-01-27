from collections import deque
board = [[0,0,0,1,1], [0,0,0,1,0],[0,1,0,1,1],[1,1,0,0,1],[0,0,0,0,0]]
result =[]
visit = []
queue = deque()
queue.append([(0, 0), (0, 1), 0])
visit.append([(0, 0), (0, 1), 0])
while queue:
    (y1, x1), (y2, x2), num = queue.popleft()
    #상
    if y1 - 1 >= 0 and visit.