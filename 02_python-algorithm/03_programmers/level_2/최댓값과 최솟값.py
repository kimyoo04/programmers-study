# https://school.programmers.co.kr/learn/courses/30/lessons/12939

'''
최댓값, 최솟값 찾으면 된다.
'''

def solution(s):
    arr = list(map(int, s.split(' ')))
    arr.sort()
    
    answer = f'{arr[0]} {arr[-1]}'
    
    return answer