import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())

stack = []
ans = []
num = 1

for i in range(N):
    v = int(input())
    if stack:
        if stack[-1] > v:
            ans.clear()
            break
        elif stack[-1] == v:
            stack.pop()
            ans.append('pop')
            continue
    while num <= v:
        stack.append(num)
        ans.append('push')
        num+=1
    ans.append('pop')
    stack.pop()

if ans:
    for v in ans:
        print(v)
else:
    print("-_-")
