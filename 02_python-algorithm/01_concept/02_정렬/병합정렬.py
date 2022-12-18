def merge_sort(unsorted_list):
    # 크기가 1이하면 반환
    if len(unsorted_list) <= 1:
      return unsorted_list
    
    # 리스트를 2분할
    mid = len(unsorted_list)//2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]
    
    # 2분할한 리스트를 각각 merge sort진행
    left_ = merge_sort(left)
    right_ = merge_sort(right)
    
    return merge(left_, right_)
  
def merge(left, right):
    i, j = 0,0 # 포인터 1개씩 사용
    sorted_list = []
    
    # left와 right를 1개씩 비교
    while i < len(left) and j < len(right):
      if left[i] < right[i]:
          sorted_list.append(left[i])
          i += 1
      else:
          sorted_list.append(right[i])
          j += 1
    # right를 이미 다 정렬한 경우
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    # left를 이미 다 정렬한 경우
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    return sorted_list