import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
from collections import deque

N = int(input())
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        if len(self.stack) == 0:
            print(-1)
        else:
            print(self.stack.pop())
    def size(self):
        print(len(self.stack))
    def empty(self):
        if len(self.stack) == 0:
            print(1)
        else:
            print(0)
    def top(self):
        if len(self.stack) == 0:
            print(-1)
        else:
            print(self.stack[-1])

st = Stack()
for _ in range(N):
    order = input().split()
    if order[0] == 'push':
        st.push(order[1])
    elif order[0] == 'pop':
        st.pop()
    elif order[0] == 'size':
        st.size()
    elif order[0] == 'empty':
        st.empty()
    elif order[0] == 'top':
        st.top()


