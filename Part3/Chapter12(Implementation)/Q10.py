#비교할 배열 생성
def makeCompareArray(array, y, x):
    compareArray = [[0] * len(array[0]) for _ in range(len(array))]
    for i in range(len(array)):
        for j in range(len(array[0])):
            if (0 <= i - y < len(array)) and (0 <= j - x < len(array[0])):
                compareArray[i][j] = array[i - y][j - x]
    return compareArray
#상하 뒤집기
def turnUpsideDown(array):
    row = len(array)
    col = len(array[0])
    for i in range(row // 2):
        tmp = array[i]
        array[i] = array[row - 1 - i]
        array[row - 1 - i] = tmp
    return array
#좌우 뒤집기
def turnLeftAndRight(array):
    row = len(array)
    col = len(array[0])
    for i in range(row):
        for j in range(col // 2):
            tmp = array[i][j]
            array[i][j] = array[i][col - 1 - j]
            array[i][col - 1 - j] = tmp
    return array
#왼쪽 대각선 기준 뒤집기
def flipLeftDiagonally(array):
    row = len(array)
    col = len(array[0])
    for i in range(row):
        for j in range(col):
            if (j > i):
                tmp = array[i][j]
                array[i][j] = array[j][i]
                array[j][i] = tmp
    return array
#오른쪽 대각선 기준 뒤집기
def flipRightDiagonally(array):
    row = len(array)
    col = len(array[0])
    for i in range(row):
        for j in range(col):
            if (j < row - 1 - i):
                tmp = array[i][j]
                array[i][j] = array[j][i]
                array[j][i] = tmp
    return array

#키인지 확인
def isCorrectKey(array, lock):
    row = len(array)
    col = len(array[0])
    for i in range(row):
        for j in range(col):
            if lock[i][j] == array[i][j]:
                return False
    return True

def find():
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

    result = 'false'
    for k in range(4):
        lock = turnUpsideDown(lock)
        lock = flipLeftDiagonally(lock)
        for i in range(-len(key),len(key),1):
            for j in range(-len(key),len(key[0]),1):
                array = makeCompareArray(key, i, j)
                print(array)
                if isCorrectKey(array, lock):
                    result = 'true'
                    return result
                turnUpsideDownArray = turnUpsideDown(array)
                if isCorrectKey(turnLeftAndRight(turnUpsideDownArray), lock):
                    result = 'true'
                    return result
                if isCorrectKey(flipRightDiagonally(turnUpsideDownArray), lock):
                    result = 'true'
                    return result
                if isCorrectKey(flipLeftDiagonally(turnUpsideDownArray), lock):
                    result = 'true'
                    return result
        print('--------------------------------')
    return False
print(find())
