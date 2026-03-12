import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
tubes = [i for i in range(1, 101)]
for _ in range(n):
    a = int(input())
    tubes.remove(a)

for x in tubes:
    print(x)

