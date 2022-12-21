# https://www.acmicpc.net/problem/10816

'''
이진탐색 상/하한선 (lower bound/upper bound) 사용
- 중복된 자료가 있을때 유용하게 탐색할 수 있는 알고리즘
- https://jackpot53.tistory.com/33
- 정렬된 상태에서만 찾을 수 있음


'''
import sys; input = sys.stdin.readline
from heapq import heappush, heappop

def lower_binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2 
        if array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start
    
def upper_binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2 
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start

n = int(input())
cards= list(map(int, input().split(" ")))
m = int(input())
array= list(map(int, input().split(" ")))
heap = []
ordered_cards = []

for card in cards:
    heappush(heap, card)    

for _ in range(n):
    ordered_cards.append(heappop(heap))

for i in range(m):
    print(upper_binary_search(ordered_cards, 0, n-1, array[i])-lower_binary_search(ordered_cards, 0, n-1, array[i]), end=' ')
    
