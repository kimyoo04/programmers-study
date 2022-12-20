def heap_sort(nums):
    from heapq import heappush, heappop
    
    heap = []
    sorted_nums = []
    
    for num in nums:
        heappush(heap, num)

    while heap:
        sorted_nums.append(heappop(heap))
        
    return sorted_nums

print(heap_sort([4, 1, 7, 3, 8, 5]))