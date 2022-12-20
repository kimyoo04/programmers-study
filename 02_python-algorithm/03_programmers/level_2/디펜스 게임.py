# https://school.programmers.co.kr/learn/courses/30/lessons/142085

from heapq import heappush, heappop, heappushpop

def solution(n, k, enemy):
    max_heap = []
    round = 0
    total = 0
    
    for enemies in enemy:
        # 적의 수 모두 더하기
        total += enemies
        
        # 준호의 병사 사용
        if total <= n:
            heappush(max_heap, -enemies)
            round += 1
            
        # 무적권 있으면 사용
        elif k > 0:
            k -= 1
            # 최대 힙 사용 및 작은 값 빼기
            # heappushpop(max_heap, -enemies)
            heappush(max_heap, -enemies)
            total += heappop(max_heap) 
            round += 1
        
        else: 
            break
    
    return round


