# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    new_arr = [arr[0]]
    prev = arr[0]

    for num in arr:
        if num != prev:
            prev = num
            new_arr.append(num)

    return new_arr