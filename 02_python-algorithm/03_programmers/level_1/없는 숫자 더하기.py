# https://school.programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    answer = 0
    num_arr = [0 for i in range(10)]

    for num in numbers:
        num_arr[num] = 1

    for indx, n in enumerate(num_arr):
        if n == 0:
            answer += indx

    return answer