# https://school.programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    min = 1000000
    min_indx = 0

    for indx, n in enumerate(arr):
        if min > n:
            min = n
            min_indx = indx
            print(min, min_indx)

    arr.pop(min_indx)

    if not arr:
        return [-1]
    else:
        return arr
