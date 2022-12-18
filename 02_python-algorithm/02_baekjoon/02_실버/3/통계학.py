# https://www.acmicpc.net/problem/2108

'''
N은 홀수, 입력되는 정수의 절댓값은 4,000 넘지 않음

산술평균 - 소수점 이하 첫째 자리 반올림, 
중앙값, 
최빈값 - 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다., 
범위
'''

import sys; input=sys.stdin.readline

# 입력 값
n = int(input())
num_list = [int(input()) for _ in range(n)]
sorted_num_list = sorted(num_list)
answer = [0] * 4

sum_value = sum(num_list)
answer[0] = round(sum_value / n)
answer[1] = sorted_num_list[n // 2]

# -4000 ~ 4000 인덱싱 + 0부터 시작으로 +1 하기
temp_list = []
count_list = [0] * 8001
for i in num_list:
    count_list[i + 4000] += 1

max_count = max(count_list) # 최빈값
for i in range(8001):
    if count_list[i] == max_count:
        temp_list.append(i)
if len(temp_list) > 1:
    answer[2] = temp_list[1] - 4000 # 여러개일 때 두 번째로 작은 값
else:
    answer[2] = temp_list[0] - 4000 # 한개일 때 가장 작은 값
  
max_value = max(num_list)
min_value = min(num_list)
range_value = max_value - min_value
answer[3] = range_value

for num in answer:
    print(num)