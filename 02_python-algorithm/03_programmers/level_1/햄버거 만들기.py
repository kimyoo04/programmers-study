def solution(ingredient):
    answer = 0
    stack = []

    for item in ingredient:
        stack.append(item)
        
        # 1,2,3,1 이 완성되면
        if stack[-4:] == [1,2,3,1]:   
            answer += 1 # 햄버거 1개 포장
            for _ in range(4):
                stack.pop() # 포장한 4개 재료 빼내기

    # answer = 상수가 포장한 햄버거 개수
    return answer