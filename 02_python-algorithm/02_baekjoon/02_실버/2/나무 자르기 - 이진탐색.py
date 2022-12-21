import sys; input = sys.stdin.readline
from heapq import heappush, heappop

def binary_search(trees, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        cut_trees = [*map(lambda x: x - mid if x > mid else 0, trees)]
        cut_len = sum(cut_trees)
        # print(cut_trees)
        # print(cut_len)
        
        if cut_len < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

N, M = map(int, input().split(" "))
trees = [*map(int, input().split(" "))]

# 오름차순 정렬
heap = []
ordered_trees = []
for tree in trees:
    heappush(heap, tree)    
for _ in range(N):
    ordered_trees.append(heappop(heap))

a = binary_search(ordered_trees, M, 0, ordered_trees[-1])
print(a)