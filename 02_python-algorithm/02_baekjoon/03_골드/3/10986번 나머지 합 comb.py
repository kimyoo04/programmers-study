import sys; input = sys.stdin.readline
from math import comb

_, m = map(int, input().split())

def sol(m: int) -> int:
    occur = [0] * m
    occur[0] = 1

    acc = 0
    for num in map(int, input().split()):
        acc = (acc + num) % m # 누적 합을 리스트에 할당하지 않고 바로 활용
        occur[acc] += 1 # 누적 합의 나머지를 그대로 카운팅
    
    # combination 연산을 모듈로 간결화
    return sum(comb(i, 2) for i in occur if i > 1) 


print(sol(m))