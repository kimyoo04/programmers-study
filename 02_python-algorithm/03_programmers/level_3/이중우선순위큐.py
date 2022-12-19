# https://school.programmers.co.kr/learn/courses/30/lessons/42628/solution_groups?language=python3

'''
주의사항: heap을 remove로 제거를 하면 n 시간복잡도이면서, 최소힙인 경우 최대가 가장 끝에 있는 것을 보장하지 않게 되는 문제가 있다. 반대의 경우도 마찬가지이다. 
-> heapify 써서 위치를 조정해야 한다.
'''

from heapq import heappush, heappop

def solution(operations):
    min_heap = []
    max_heap = []
    count = 0
    
    for operation in operations:
        char, num = operation.split(" ")
        num = int(num)
        
        if char == "I":
            count += 1
            heappush(min_heap, num)    
            heappush(max_heap, -num)    
        elif count != 0 and char == "D":
            count -= 1
            if num == 1:
                max_num = heappop(max_heap)    
                min_heap.remove(-max_num)
            else:
                min_num = heappop(min_heap)
                max_heap.remove(-min_num)
                
    if count == 0:
        answer = [0, 0]
    else:
        answer = [-heappop(max_heap), heappop(min_heap)]
    
    return answer
