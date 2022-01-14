chess_board_x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
chess_board_y = ['1', '2', '3', '4', '5', '6', '7', '8']
steps = []
a, b = 1, 2
for i in range(2):
    a, b = b, a
    for j in range(2):
        a *= -1
        for k in range(2):
            b *= -1
            steps.append((a, b))
print(steps)
input_data = input()
index_x = chess_board_x.index(input_data[0])
index_y = chess_board_y.index(input_data[1])

cnt = 0
for step in steps:
    next_x = index_x + step[0]
    next_y = index_y + step[1]
    if 0 <= next_x < 8 and 0 <= next_y < 8:
        cnt += 1
print(cnt)