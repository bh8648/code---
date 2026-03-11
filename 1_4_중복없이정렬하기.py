# 첫째 줄에 숫자의 개수 N(1<=N<=100)이 주어진다.

# 둘째 줄에 N개의 정수(1~1000)가 주어진다. 

# 주어지는 N개의 정수를 중복 없이 내림차순 정렬하여 출력한다.

"""
파이썬은 input이 너무 느림
코테에서는 input도 sys에서 설정을 해줘야 함.
"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())

buf = list(set(map(int, input().split())))
buf.sort(reverse=True)
print(*buf)



import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
s = set(arr)
arr = list(s)

arr.sort(reverse=True)
print(*arr)

