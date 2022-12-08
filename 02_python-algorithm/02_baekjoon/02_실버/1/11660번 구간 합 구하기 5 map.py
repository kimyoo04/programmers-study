# https://www.acmicpc.net/problem/11660
import sys; input = sys.stdin.readline

n,m = map(int,input().split())
dp = [[0 for _ in range(n+1)]]

for i in range(n):
    temp = [*map(int,input().split())] # 맵 객체가 바뀜
    accum = 0; tdp = [0]
    for j in range(n):
        accum += dp[i][j+1] + temp[j] - dp[i][j]
        tdp.append(accum)
    dp.append(tdp)

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])