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
search_datas=[]
Q = int(input())
for _ in range(Q):
    search_datas.append(list(map(int, input().split())))

for search_data in search_datas:
    ids = dict()
    for i, v in enumerate(search_data):
        if v != -1:
            ids[i] = v
    # -1이 아닌 값들의 인덱스와 해당 값을 저장
    # row의 인덱스와 값을 비교
    count = 0
    for row in rows:
        check = True
        for k in ids:
            if row[k] != ids[k]:
                check = False
        if check:
            count += 1
    print(count)

