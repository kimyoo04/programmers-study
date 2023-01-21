'''
K = 오영식이 가진 랜선 개수
N = 박성원은 랜선을 모두 N개의 같은 길이의 랜선 만들기

설명
- K개의 랜선으로 N개의 랜선을 만들 수 없는 경우 없다.
- 자를 때 cm 단위로 정수길이만큼 자른다.
- N개보다 많이 만드는 것도 N개를 만드는 것에 포함

구할 값
- 만들 수 있는 최대 랜선 길이를 구하는 프로그램

조건
- 1 <= K <= 10000
- 1 <= N <= 1000000
- K <= N

핵심
- 1, 2, 3, 4 번째 선들을 나눈 몫을 다 더해 K개 이상이 되야함
- K개 이상이 될 때 나눈 값이 최대를 찾도록 이진탐색을 해야함.
'''

import sys; input = sys.stdin.readline
from heapq import heappush, heappop


def binary_search(array, target, start, end):
    mid = (start + end) // 2
    
    while start <= end:
        cnt = 0
        
        
        
        if cnt < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result 


def heap_sort(array):
    heap = []
    sorted_list = []
    
    for item in array:
        heappush(heap, item)

    for _ in range(len(array)):
        sorted_list.append(heappop(heap))
    
    return sorted_list


N, K = map(int, input().split(" "))
lenlines = []
for _ in range(N):
    lenlines.append(int(input()))

