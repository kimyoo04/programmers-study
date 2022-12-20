from heapq import heappush, heappop

'''
입력값
---------------------------------------------
n = 준호의 병사 (적 1명 죽임)
m = 준호의 기사 (적 2명 죽임)
k = 무적권 스킬
enemy = 라운드마다 나타날 적의 수 1차원 배열
---------------------------------------------
테스트 케이스
---------------------------------------------
1)
입력
3, 4, 4, [3, 3, 2, 3, 3, 4, 4, 4, 4, 4]
출력
[5, 6, 7, 8]
---------------------------------------------
2)
입력
5, 4, 4, [3, 3, 2, 3, 3, 4, 4, 4, 4, 4]
출력
[5, 6, 7, 8]
---------------------------------------------
'''

def solution(n, m, k, enemy):
    round_cnt = len(enemy)
    
    # 무적권 스킬 수가 라운드 수보다 큰 경우
    if k >= round_cnt: return [x+1 for x in range(k)]
    
    # k 길이의 (enemies, round)로 이루어진 최소 힙 생성
    enemy_min_heap = []
    for round_, round_enemy in enumerate(enemy[:k], 1):
        heappush(enemy_min_heap, (round_enemy, round_))
    # print(enemy_min_heap)

    for round_, round_enemy in enumerate(enemy[k:], k + 1):
        # print(round_, round_enemy)
        # 최소 힙 루트 노드와 다음 라운드 적 수 비교
        if enemy_min_heap[0][0] < round_enemy:
            backup = enemy_min_heap[:] # 복사 <------------------- 비효율적임 
            heappush(enemy_min_heap, (round_enemy, round_))
            round_enemy = heappop(enemy_min_heap)[0]
        
        # 최대한 기사를 먼저 사용
        if round_enemy and m:
            while m:
                if round_enemy > 1:
                    round_enemy -= 2
                    m -= 1
                else:
                    break
            
        # 병사가 0 이하면 break
        if round_enemy and n:            
            n -= round_enemy
            if n > 0:
                continue
            elif n == 0:
                break
            else:
                enemy_min_heap = backup
                break
        elif round_enemy and n <= 0:
            enemy_min_heap = backup
            break
        else:
            continue
        
    # print(n, m)

    # k가 쓰인 라운드 생성   
    rounds_min_heap = []
    k_used_rounds = []

    # 힙 정렬
    for round_enemy, round_ in enemy_min_heap:
        heappush(rounds_min_heap, round_)
    while rounds_min_heap:
        k_used_rounds.append(heappop(rounds_min_heap))

    # n 이 음수가 되면 k를 사용한 라운드를 순서대로 1차원 배열로 반환
    if n <= 0 and m <= 0: return k_used_rounds
    else: return k_used_rounds

# a = solution(5, 4, 4, [3, 3, 2, 3, 3, 4, 4, 4, 4, 4])
a = solution(7, 3, 3, [4, 2, 4, 5, 3, 3, 1, 4, 3])
print(a)