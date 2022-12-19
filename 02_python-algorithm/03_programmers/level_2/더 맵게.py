# https://school.programmers.co.kr/learn/courses/30/lessons/42626

'''
- try except로 오류 처리를 해주는 것 이 핵심
- heap 자료 구조 활용 
- min_heap[0]이 K보다 작은 동안 조건 설정 
'''

from heapq import heappush, heappop

def solution(scoville, K):
    min_heap = []
    count = 0
    
    for num in scoville:
        heappush(min_heap, num)
    
    # min_heap에 K보다 작은 값이 있는 동안
    while min_heap[0] < K :
        try:
            heappush(min_heap, heappop(min_heap) + heappop(min_heap) * 2)
        except IndexError:
            return -1
          
        count += 1
    return count