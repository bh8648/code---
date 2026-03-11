# 첫 줄에 수의 개수 N(1≤N≤100,000)이 주어진다.
# 다음 N개의 줄에 수들이 주어진다. 모든 수는 0이상 1,000,000이하이다.

# 주어진 수들을 오름차순 정렬하여 각 줄에 숫자 한개씩 출력한다.

import sys
sys.setrecursionlimit(10000)

buf = []
N = int(input())
for _ in range(N):
    n = int(input())
    buf.append(n)

buf.sort()

for x in buf:
    print(x)



