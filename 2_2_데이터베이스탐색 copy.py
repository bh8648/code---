import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 길이 M 데이터는 N개

# 탐색 요청시 찾을 데이터 길이는 M
# 탐색시 데이터 일부만 주어질수도 있음

# -1은 어떤 데이터가 존재하더라도 무관함

N, M = map(int, input().split())
rows = []
for _ in range(N):
    rows.append(list(map(int, input().split()))) # A
Q = int(input())

def ismatch(a,b):
    for i in range(M):
        if b[i] == -1:
            continue
        if b[i] != a[i]:
            return False
    return True

for _ in range(Q):
    s = list(map(int, input().split()))
    count = 0
    for row in rows:
        if ismatch(row, s):
            count += 1
    print(count)


