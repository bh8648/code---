import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


# 개미 -> 오른쪽으로 감 / 오른쪽 벽이 막혀있으면 아래로 감 -> 더이상 못움직이면 탐험을 끝냄

food = 0

H, W = map(int, input().split())
stop_check = False
path = [list(map(int, input().split())) for i in range(H)]

# 오른쪽을 체크해서 갈 수 있다면(현재 인덱스+1이 1이 아니라면) 오른쪽으로 이동하고 *로 바꿈
j_check = 0
for i in range(H):  
    for j in range(j_check, W):
        if path[i][j] == 2:
            food += 2
        path[i][j] = '*'
        if ((j+1 < W) and (path[i][j+1] == 1)):
            j_check = j
            break
        if j == W-1:
            j_check = j
    if i+1 < H and path[i+1][j_check] == 1:
        break
        
   
print(food)
for x in path:
    print(*x)


print("============================================================")
# 오른쪽 끝에서 시작해서 왼쪽으로 가다가 아래로 내려가게 만들기

import sys
sys.setrecursionlimit(10000)
sys.stdin.readline

H, W = map(int, input().split())
path = [list(map(int, input().split())) for _ in range(H)]

x, y = 0,W-1
food = 0
while True:
    if path[x][y] == 2:
        food += 2
    path[x][y] = '*'

    if y-1 >= 0 and path[x][y-1] != 1:
        y -= 1
    elif x+1 < H and path[x+1][y] != 1:
        x += 1
    else:
        break

print(food)
for x in path:
    print(*x)
























