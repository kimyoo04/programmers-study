# https://school.programmers.co.kr/learn/courses/30/lessons/142085

from heapq import heapify, heappush, heappop

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
            heappush(max_heap, -enemies)
            total += heappop(max_heap) 
            round += 1
        
        else: 
            break
    
    return round


def solution1(n, k, enemy):
    round_cnt = len(enemy)
    
    if k >= round_cnt: return round_cnt
    
    # k 개 길이의 최소 힙 생성
    min_heap = enemy[:k]
    heapify(min_heap)

    for stage, stage_enemy in enumerate(enemy[k:], k + 1):
        print(stage, stage_enemy)
        
        # 최소 힙 루트 노드와 다음 라운드 적 수 비교
        if min_heap[0] < stage_enemy:
            heappush(min_heap, stage_enemy)
            stage_enemy = heappop(min_heap)
        
        # 위의 비교 따라서 준호의 병사 수 n - stage_enemy
        n -= stage_enemy
        
        # n 이 음수가 되면 성공한 stage 값 반환 후 게임 종료
        if n < 0: return stage - 1
    
    # 게임 종료
    return round_cnt


a = solution1(7, 3, [4,2,4,5,3,3,1])
print(a)