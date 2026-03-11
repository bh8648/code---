# 첫 줄에 학생 수 N (1≤N≤10) 이 주어집니다.
# 두 번째 줄 부터 N줄 동안 이름, 달리기 점수, 팔굽혀펴기 점수, 윗몸일으키기 점수가 주어집니다.
# 이름 길이는 10글자 보다 작습니다. 

"""
5
Messi 50 70 40
Mbappe 70 40 60
Modric 80 50 60
Neymar 100 60 50
Ronaldo 100 70 50
"""

"""
파이썬은 input이 너무 느림
코테에서는 input도 sys에서 설정을 해줘야 함.
"""
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

students = []
N = int(input())
for _ in range(N):
    name, score1, score2, score3 = input().split()
    score1 = int(score1)
    score2 = int(score2)
    score3 = int(score3)
    students.append([name, int(score1), int(score2), int(score3)])

# 2차원 배열에서 어떤 컬럼의 값을 써서 정렬할지 정하는 옵션 sort(key=)를 사용
students.sort(key= lambda v : (v[1], v[1]+v[2]+v[3]), reverse=True)
for v in students:
    print(v[0])
print()

students.sort(key= lambda v : (v[2], v[1]+v[2]+v[3]), reverse=True)
for v in students:
    print(v[0])
print()

students.sort(key= lambda v : (v[3], v[1]+v[2]+v[3]), reverse=True)
for v in students:
    print(v[0])
