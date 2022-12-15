'''
입력:
T = 테스트 케이스
k = 각 케이스마다 입력
n = 두번째 줄 정수

계약조건:
“a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다”
-> 바로 아래층의 1~b호의 사람을 다 더한만큼 살아야한다.
바로 아래층의 구간합

출력:
k층 n호에 몇명 사는지

제한:
1 ≤ k, n ≤ 14

단:
아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
'''

import sys
input = sys.stdin.readline

# 15x15 리스트
D = [[0 for j in range(15)] for i in range(15)]

# 0층 거주자 1~14명 채우기
for i in range(1,15):
    # 각 층의 1호 채우기
    D[i][1] = 1
    # 0층의 각 호별 거주자 채우기
    D[0][i] = i

for floor in range(1, len(D)):
    for ho in range(1, len(D[floor])-1):
        D[floor][ho+1] = D[floor][ho] + D[floor-1][ho+1]
print(D)

T = int(input())
for i in range(0, T):
    K = int(input())
    N = int(input())
    print(D[K][N])



