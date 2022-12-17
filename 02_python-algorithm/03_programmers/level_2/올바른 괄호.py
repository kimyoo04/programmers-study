def solution(s):
    stack = []
    answer = True
    
    for i in s:
        # 빈 stack, ( 이면
        if not stack and i == "(":
            stack.append(i)
        # stack은 (, i는 ) 이면 - ( 와 ) 이 만나면
        elif stack and stack[-1] == "(" and i == ")":
            stack.pop()
        # 비지 않은 stack, ( 이면
        elif stack and i == "(":
            stack.append(i)
        else:
            return False
    
    # 빈 stack 이면 True
    if not stack:
        return True
    else:
        return False