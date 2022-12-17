# https://school.programmers.co.kr/learn/courses/30/lessons/12924?language=python3

'''
n 값이 들어오면 n 이하의 수들을 활용함 -> range(1,n) 활용

예제를 봤을 때 순차적으로 숫자들이 더해지는 모습이 있다. -> 투 포인터

제한사항은 n이 10000 이하라서 시간복잡도 n^2만 피하면 된다.
'''

# 투 포인터
def solution(n):
    start_index = 0
    end_index = 0
    count = 1 # 자기 자신 + 1
    sum = 0

    while end_index != n:
        if sum > n:
            sum -= start_index
            start_index += 1
        elif sum < n:    
            end_index += 1
            sum += end_index
        else:
            count += 1
            end_index += 1
            sum += end_index

    return count

# 약수?
def solution1(n):
    count = 0
    
    for i in range(1,n+1) :
        if i % 2 != 0 and n % i == 0 :
            count += 1

    return count

# 완전 탐색
def solution2(n):
    mid = (n // 2) + 1 # 2 로 약분해서 범위 줄임
    count = 1
    for i in range(1, mid):
        val = 0
        for j in range(i, mid+1):
            val += j
            if val == n:
                count += 1
                break
            if val > n:
                break
    return count