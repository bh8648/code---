import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
from collections import deque
N = int(input())

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def push(self, data):
        self.queue.append(data)
    def pop(self):
        if self.is_empty():
            print(-1)
        else:
            print(self.queue.popleft())
    def size(self):
        print(len(self.queue))
    def empty(self):
        if self.is_empty():
            print(1)
        else:
            print(0)
    def front(self):
        if self.is_empty():
            print(-1)
        else:
            print(self.queue[0])
    def back(self):
        if self.is_empty():
            print(-1)
        else:
            print(self.queue[-1])        
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False

q1 = Queue()
for _ in range(N):
    order = input().split()
    if order[0] == 'push':
        q1.push(order[1])
    elif order[0] == 'pop':
        q1.pop()
    elif order[0] == 'size':
        q1.size()
    elif order[0] == 'empty':
        q1.empty()
    elif order[0] == 'front':
        q1.front()
    elif order[0] == 'back':
        q1.back()

