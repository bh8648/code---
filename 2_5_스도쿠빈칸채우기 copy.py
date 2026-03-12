import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

matrix = [input().strip() for i in range(9)]
checker = [i for i in range(1,10)]

for row in matrix:
    if "?" in row:
        for i, c in enumerate(row):
            if c != "?":
                checker.remove(int(c))

print(*checker)



# print(result)
