import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    coffes = []
    cnt = dict()
    prices = []
    for _ in range(N):
        c = int(input())
        coffes.append(c) # 직원들이 원하는 커피의 종류
        cnt[c] = 0
    for x in coffes:
        cnt[x] += 1
    for i in range(M):
        prices.append(int(input()))
    price_i = 0
    for key in cnt:
        cnt[key] *= prices[price_i]
        price_i += 1
    total_p = 0
    for key in cnt:
        total_p += cnt[key]

    if K-total_p >= 0:
        print("Y")
    else:
        print("N")

# 딕셔너리로 구성해서 커피 종류의 개수를 카운팅한다음 순차적으로 가격을 카운팅 개수와 곱해서 총합을 구함. 카드 한도와 비교

