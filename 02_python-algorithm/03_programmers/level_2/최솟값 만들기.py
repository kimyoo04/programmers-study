# https://school.programmers.co.kr/learn/courses/30/lessons/12941

'''
두 리스트에서 뺀 값의 누적 합은 오름차순과 내림차순으로 곱해야 최소가 될 것이다.
'''

def solution(A,B):
    answer = 0
    A.sort(reverse=True)
    B.sort()
    
    for i in range(len(B)):
        answer += A[i] * B[i]

    return answer