# https://www.acmicpc.net/problem/11659

'''
- 합 배열 S를 만들면 기존 리스트의 일정 범위으 합을 구하는 시간 복잡도가 O(N)에서 O(1)로 감소한다.
- S[i] = S[i-1] + A[i]
- i부터 j까지 구간합 = S[j] - S[i-1]
'''

import sys
input = sys.stdin.readline # 시간초괴 때문에 할당

N, M = map(int, input().split()) # 데이터의 개수, 질의 개수
num_list = list(map(int, input().split())) # 구간 합을 구할 대상 배열
sum_list = [0]
temp = 0

for num in num_list:
    temp = temp + num
    sum_list.append(temp)
    
for _ in range(0, M):
    i, j = map(int, input().split())
    print(sum_list[j] - sum_list[i-1])