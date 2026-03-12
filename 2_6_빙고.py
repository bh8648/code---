import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

matrix = [list(map(int, input().split())) for i in range(5)]
checks = list(map(int,(input().split())))
result = 0
break_check = False
for check in checks:
    result += 1
    # 값 바꾸기
    for row in matrix:
        for i, v in enumerate(row):
            if v == check:
                row[i] = -1

    # 바뀐 값 체크(행 빙고)
    for row in matrix:
        if row.count(-1) == 5:
            break_check = True
    
    # 바뀐 값 체크(열 빙고)
    for i in range(5):
        if all(matrix[j][i] == -1 for j in range(5)):
            break_check = True

    # 바뀐 값 체크(대각 빙고)
    if all((matrix[i][i] == -1 for i in range(5))):
        break_check = True
    if all((matrix[i][4-i] == -1 for i in range(5))):
        break_check = True

    if break_check:
        break

print(result)


