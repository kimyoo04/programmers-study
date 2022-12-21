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

# 참고 - https://jackpot53.tistory.com/33