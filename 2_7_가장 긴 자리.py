import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

H, W = map(int, input().split())

matrix = [list(map(int, input().split())) for i in range(H)]

# 반복문을 돌리다가 1을 만나면 거기서 수를 그만 헤아림
# 반복문을 체크 하는건 가로 또는 세로 방식

max_check = 0
for row in matrix:    
    row_check = 0
    for x in row:
        if x == 1:
            row_check = 0
        else:
            row_check += 1
        if max_check < row_check:
            max_check = row_check

for i in range(W):
    col_check = 0
    for j in range(H):
        if matrix[j][i] == 1:
            col_check = 0
        else:
            col_check += 1
        if max_check < col_check :
            max_check = col_check

print(max_check)








