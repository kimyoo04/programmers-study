# https://school.programmers.co.kr/learn/courses/30/lessons/42897

'''
문제 설명
- 도둑이 마을을 털 계획함
- 그림처럼 집 배치
- 서로 인접한 집들과 방법장치 연결 -> 인접한 두 집 털면 경보
- 각 집에 돈이 담긴 배열 money
- 도둑이 훔칠 수 있는 돈 최댓값 return
'''

'''
핵심
- 원순열
- 1차원 배열
- 인접한 값 건너 뛰기
- dp
- 탐색 (?)
- 마이너스 인덱싱

분석
- dp(1) = o = 1개씩 1가지
- dp(2) = o o = 1개씩 2가지
- dp(3) = o o o = 1개씩 3가지, 2개씩 1가지
- dp(4) = o o o o = 1개씩 4가지, 2개씩 2가지
- dp(5) = o o o o o = 1개씩 5가지, 2개씩 3가지, 3개씩 1가지
- dp(6) = o o o o o o = 1개씩 6가지, 2개씩 4가지, 3개씩 2가지
.
.
- dp(n) = 
num = math.ceil(n/2) 
num을 기준으로 1부터 num까지 n에 나눈 몫의 합
'''

# 첫번째 실패한 시도
import math

def solution1(money):
    max = 0

    n = len(money)
    max_houses = math.ceil(n / 2)
    
    # 큰 수 부터 체크
    for num in range(max_houses, 0, -1):
        cycle = n // num
        start = 0
        end = 0
        
        # end = 0    n - 1 = 4 - 1 = 3
        # money 의 인덱스 = [0, 1, 2, 3]
        while end < n - 1:
            sum = 0
            
            if num == 1:
                sum += money[start]
                end = start
            # 2 이상인 경우 건너뛰기
            else: 
                # step = 0, 1   cycle = 2   start = 1   end = 1, 3
                for step in range(cycle):
                    sum += money[start + step * 2]
                end = start + step * 2
                
            # 최댓값 구하기
            if sum > max:
                max = sum
                
            start += 1

    answer = max
    return answer


'''
틀린 이유
- 1 칸 건너뛰기만 수행했기 때문
'''

# 두 번째 실패한 시도

import math

def solution(money):
    max = 0
    length = len(money)
    max_houses = math.ceil(length / 2)
    
    # 큰 수 부터 체크
    for num in range(max_houses, 0, -1):
        cycle = length // num

        
        # end = 0    n - 1 = 4 - 1 = 3
        # money 의 인덱스 = [0, 1, 2, 3]
        # step = 2, 3
        for step in range(2, length):
            start = 0
            end = 0
            
            while end < length - 1:
                sum = 0

                # 1 인 경우
                if num == 1:
                    sum += money[start]
                    end = start
                    start += 1

                # 1 초과 경우 건너뛰기 사용
                else: 
                    # i = 0, 1   cycle = 2   start = 1   end = 1, 3
                    for i in range(cycle):
                        end = start + i * step
                        if end < length - 1:
                            # print("num", num, "start", start, "step", step, "인덱스", start + i * step)
                            sum += money[start + i * step]
                    start += 1
                # 최댓값 구하기
                if sum > max:
                    max = sum
            # print(max)
    answer = max
    return answer
    

'''
틀린 이유
- 1번 씩 건너뛰기를 기준으로 제일 끝 인덱스가 나왔을 때 루프를 탈출함으로 모든 검색을 하지 못하고 끝나버림.

해결법
- 건너뛰기 방식을 나눈 나머지로 처리한 후, 넣어진 index 들의 좌우 숫자 비교를 하는 것으로 sum을 구하는
방식이 떠올랐다.
'''