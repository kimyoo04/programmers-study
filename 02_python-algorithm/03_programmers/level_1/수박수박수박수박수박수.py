def solution(n):
    answer = ''
    
    # for 문
    for i in range(1, n+1):
        # 짝수 홀수 구분
        if i % 2 != 0:
            answer += "수"
        else:
            answer += "박"

    # 출력값 전달
    return answer