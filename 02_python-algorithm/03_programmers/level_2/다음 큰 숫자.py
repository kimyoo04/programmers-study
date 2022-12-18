# https://school.programmers.co.kr/learn/courses/30/lessons/12911?language=python3

'''
2진수로 변환을 할줄아는지 묻는다.
bin()함수의 반환 타입이 문자열이다! 그래서 count() 메소드 사용 가능

count()메소드 사용을 몰랐다면 collections의 Counter도 가능
'''

def solution(n):
    c = bin(n).count('1')
    for m in range(n+1,1000001):
        if bin(m).count('1') == c:
            return m

# 2진수 변환 함수1
def get_binary1(n):
    if n == 0: return ''
    elif n % 2 == 0: return get_binary1(n // 2) + '0'
    else: return get_binary1(n // 2) + '1'
    
# 2진수 변환 함수2
def get_binary2(n, lists):
    a, b = divmod(n, 2) # Return the tuple (x//y, x%y)
    lists.append(b)
    if a == 0 :
        return lists
    else :
        return get_binary2(a, lists)
