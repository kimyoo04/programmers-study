# https://school.programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):
    multiple = 1
    arr_len = len(arr)

    for num in arr:
        multiple *= num

    for k in range(2, multiple):
        count = 0

        for i in arr:
            if k % i == 0:
                count += 1
        if count == arr_len:
            return k

    return multiple