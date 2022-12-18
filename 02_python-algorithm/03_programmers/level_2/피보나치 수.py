# https://school.programmers.co.kr/learn/courses/30/lessons/12945?language=python3

def solution(n):
    F = [0, 1]
    for i in range(2, n+1):
        F.append(F[i-1] + F[i-2])
    
    answer = F[n] % 1234567 
    return answer

def solution1(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    
    answer = a % 1234567 
    return answer