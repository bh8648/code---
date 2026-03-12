import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


H, W = map(int, input().split())

rows = []
for _ in range(H):
    rows.append(list(map(int, input().split())))

Q = int(input())
for _ in range(Q):
    t, v = map(int, input().split())
    if t == 0:
        print(*rows[v])
    elif t == 1 :
        cols = []
        for i in range(len(rows)):
            cols.append(rows[i][v])
        print(*cols)

