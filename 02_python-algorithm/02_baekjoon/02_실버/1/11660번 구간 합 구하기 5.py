# https://www.acmicpc.net/problem/11660

import sys
input = sys.stdin.readline

# n 리스트 크기, m 질의 수
# A 원본 리스트, D 합 리스트
n, m = map(int, input().split())
A_list = [[0] * (n+1)]
S_list = [[0] * (n+1) for _ in range(n+1)] # 리스트 컴프리헨션

# 원본 리스트 저장
for i in range(n):
  A_row = [0] + [int(x) for x in input().split()]
  A_list.append(A_row)

# 합 리스트 저장
for i in range(1, n+1):
  for j in range(1, n+1):
    S_list[i][j] = S_list[i][j-1] + S_list[i-1][j] - S_list[i-1][j-1] + A_list[i][j]

# 구간 합 계산
for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  x1 -= 1
  y1 -= 1
  result = S_list[x2][y2] - S_list[x1][y2] - S_list[x2][y1] + S_list[x1][y1]
  print(result)