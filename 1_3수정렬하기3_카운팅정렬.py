# 첫 줄에 수의 개수 N(1≤N≤10,000,000)이 주어진다.
# 다음 N개의 줄에 수들이 주어진다. 모든 수는 0이상 10,000이하이다.

# 주어진 수들을 오름차순 정렬하여 각 줄에 숫자 한개씩 출력한다.

# 메모리 제한이 12MB -> 카운팅 정렬 하라는 뜻. 정수를 저장할 공간이 부족


"""
파이썬은 input이 너무 느림
코테에서는 input도 sys에서 설정을 해줘야 함.
"""
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


N = int(input())
cnt = [0 for i in range(10001)]

for _ in range(N):
    i = int(input())
    cnt[i] += 1

for i,v in enumerate(cnt):
    for _ in range(v):
        print(i)





N = int(input())
cnt = [0 for i in range(10001)]

for _ in range(N):
    v = int(input())
    cnt[v] += 1

for i in range(10001):
    for j in range(cnt[i]):
        print(i)