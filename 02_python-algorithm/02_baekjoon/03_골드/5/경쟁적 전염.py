# https://www.acmicpc.net/problem/18405

'''
문제
- NxN 크기의 시험관
- 바이러스는 상하좌우 증식
- 번호가 낮은 종류의 바이러스부터 먼저 증식
- 특정한 칸에 이미 어떠한 바이러스가 존재하면, 그 곳에 다른 바이러스가 증식 불가

-> S초가 지난 후 (X,Y)에 존재하는 바이러스의 종류를 출력
-> 만약 S초 후 (X,Y)에 바이러스가 존재하지 않는다면, 0을 출력

(가장 왼쪽 위에 해당하는 곳은 (1,1)에 해당)

input
- N, K가 공백을 기준으로 구분 (1 ≤ N ≤ 200, 1 ≤ K ≤ 1,000)
- 둘째 줄부터 N개의 줄에 걸쳐서 시험관의 정보
- 각 행은 N개의 원소로 구성
- 바이러스의 번호가 공백을 기준으로 구분
- 바이러스가 존재하지 않는 경우 0
- 바이러스의 번호는 K이하의 자연수
- N+2번째 줄에는 S, X, Y가 공백을 기준으로 구분되어 주어진다.
(0 ≤ S ≤ 10,000, 1 ≤ X, Y ≤ N)
'''

'''
핵심
- 바이러스 번호가 작을수록 우선 (큐 선입선출)
- 1초 증가마다 바이러스가 퍼진 셀마다 append 시키기
- S초 이후 중지 후, X-1, Y-1 좌표의 셀 출력
- S초 이후 중지를 위해선 바이러스의 퍼지는 시간을 체킹할 것 (virus_num, time, x, y)
- 시험관 안에 위치하는 것을 확인 0 < X < N, 0 < Y < N

BFS 인 이유?
-
'''

import sys
input = sys.stdin.readline
from collections import deque


def solution():
    # N 시험관 크기
    # K 바이러스 번호 수
    N, K = map(int, input().split())

    # matrix 시험관
    matrix = []

    # virus 바이러스 모음
    virus = []

    # 이동좌표: 상 하 좌 우
    mx = [0, 0, -1, 1]
    my = [-1, 1, 0 , 0]

    for i in range(N):
        matrix.append(list(map(int, input().split())))
        for j, cell in enumerate(matrix[i]):
            if cell != 0:
                virus.append((cell, 0, i, j))

    len_virus = len(virus)

    # 작은 것부터 퍼지기 때문에 정렬 및 큐 사용
    virus.sort(key=lambda x: x[0])
    queue = deque(virus)

    # S 시간
    # X, Y 행렬 좌표
    S, X, Y = map(int, input().split())
    X -= 1
    Y -= 1

    while queue:
        virus_num, time, x, y = queue.popleft()

        if time == S:
            break

        # 상 하 좌 우 4번 반복 및 필터링
        for i in range(4):
            new_x = x + mx[i]
            new_y = y + my[i]

            # 시험관 안에 있고, 빈 셀(0)이면
            if 0 <= new_x < N and 0<= new_y < N and matrix[new_x][new_y] == 0:
                matrix[new_x][new_y] = virus_num
                queue.append((virus_num, time+1, new_x, new_y))

    return(matrix[X][Y])


if __name__ == "__main__":
    print(solution())