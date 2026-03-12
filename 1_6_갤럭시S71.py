"""
갤럭시S 71 이 출시한다. 매일 갤럭시S 71 N개를 상자에 포장하여 판매점으로 보내는 일을 하고있다. 우리에겐 크기가 다른 상자 K개가 있으며, 최대한 적은 수의 상자를 사용하고 싶다. 
포장한 후 상자에 여유 공간이 많아도 상관없다.
갤럭시S 71의 상자는 가로1, 세로1, 높이1 이며 상자의 높이는 모두 1이고, 가로세로의 크기는 다양하다.
N과 상자 정보들이 주어졌을 때 몇 개의 상자가 필요한지 출력하자.
"""

# 첫 줄에 필요한 갤럭시S 71의 수 N(1≤N≤10000)과, 상자의 수 K(1≤K≤10000)가 주어진다.
# 다음 K 개의 줄에 상자의 가로, 세로(1≤가로,세로≤1000) 크기가 주어진다. 모든 상자를 사용하였을 때 N개 이상을 포장할 수있도록 주어진다.

# 최소 필요한 상자수를 출력한다.

"""
파이썬은 input이 너무 느림
코테에서는 input도 sys에서 설정을 해줘야 함.
"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

boxes = []
N, K = map(int, input().split())
for x in range(K):
    garo, sero = map(int, input().split())
    boxes.append(garo*sero)

boxes.sort(reverse=True)
for i in range(K):
    N -= boxes[i]
    if N <= 0 :
        print(i+1)
        break

