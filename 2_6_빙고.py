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


import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

matrix = [list(map(int, input().split())) for _ in range(5)]
calls = list(map(int, input().split()))

# 1. 돌면서 사회자가 부른 값을 만나면 -1로 바꿈
def func():
    count = 0
    for call in calls:
        count += 1
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == call :
                    matrix[i][j] = -1
        # -1로 바꾸고 난 다음 체크했는데 빙고가 완성되면? 상황종료 후 그 값을 출력
        
        # 가로 빙고
        for i in range(5):
            if all(matrix[i][j] == -1 for j in range(5)):
                return count

        # 세로 빙고
        for i in range(5):
            col_cnt = 0
            for j in range(5):
                if matrix[j][i] == -1:
                    col_cnt += 1
                if col_cnt == 5:
                    return count
        # 대각선 빙고 2개
        cnt3 = 0
        for i in range(5):
            if matrix[i][i] == -1:
                cnt3 += 1
            if cnt3 == 5:
                return count
        cnt4 = 0
        for i in range(5):
            if matrix[i][4-i] == -1:
                cnt4 += 1
            if cnt4 == 5:
                return count

print(func())




def removeNumber(v):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == v:
                matrix[i][j] = -1


