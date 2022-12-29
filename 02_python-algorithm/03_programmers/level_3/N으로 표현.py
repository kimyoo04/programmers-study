# https://school.programmers.co.kr/learn/courses/30/lessons/42895

'''
dp(5, 1) = 5
dp(5, 2) = 5+5, 5-5, 5*5, 5/5, 55
dp(5, 3) = (5+5)+5, (5+5)-5, (5+5)*5, (5+5)/5, 5-(5+5)... 555
.
.
cnt=1, 1씩 증가 반복

dp(N, cnt) = 4(dp(N, cnt-1)) + 1
dp 함수는 set 자료 반환

dp 함수의 결과에서 number 일치하는지 탐색, cnt 반환
'''

# 실패한 코드
def get_array(N, number, results, cnt):
    if cnt > 8:
        return -1
    
    new_results = results.copy()
    new_results.add(int(str(N)*cnt)) 
    
    for num in results:
        new_results.add(num+N)
        new_results.add(num-N)
        new_results.add(N-num)
        new_results.add(num*N)
        if num != 0:
            new_results.add(num//N)
            new_results.add(N//num)
        
    print(new_results, cnt, len(new_results))
    if number in new_results:
        return cnt
    else:
        return get_array(N, number, new_results, cnt+1)    
    
def solution1(N, number):
    if N == number:
        return 1
    
    cnt = 2
    results = set() # <- {}
    results.add(N) # <- {5}
    answer = get_array(N, number, results, cnt)
    return answer

'''

문제점
- 재귀 방식으로 처리는 복잡함을 느낌
- 5, 55, 555, 5555, 55555... 숫자가 각각의 최대값이 되기 때문에 이 숫자를 기준으로 잡기
- 마이너스 연산 때문에 a - b, b - a 의 과정 거치기
- 모든 경우의 수를 얻기 위해 1~8까지의 과정에서 모든 경우의 수를 다 연산시키도록 이중 for 문을 이용

이해 참고 - https://alreadyusedadress.tistory.com/115
'''

# 답 코드1
def solution2(NUM, number):
    arr = [[]] + [[int(str(NUM) * i)] for i in range(1,9)]
    if [number] in arr:
        return arr.index([number])

    for i in range(2, 9):
        for j in range(1, i):
            for a in arr[j]: # (1, n-1) 부터 (n-1, 1)까지 연산
                for b in arr[i-j]:
                    arr[i].append(a + b)
                    arr[i].append(a * b)
                    arr[i].append(a - b)
                    if 0 != b:
                        arr[i].append(a // b)
        # 중복 제거
        arr[i] = list(set(arr[i]))
        print(arr[i], i, len(arr[i]))
        if number in arr[i]:
            return i
    return -1

# 답 코드2
def solution3(N, number):
    if number == 1:
        return 1
    set_list = []
    
    for cnt in range(1, 9): # 1개부터 8개까지 확인
        partial_set = set()
        partial_set.add(int(str(N) * cnt)) # 이어 붙여서 만드는 경우 넣기
        for index in range(cnt - 1): # (1, n-1) 부터 (n-1, 1)까지 연산
            for op1 in set_list[index]:
                for op2 in set_list[-index - 1]:
                    print(f'cnt={cnt} \nset_list={set_list} \nindex={index} \nop1={op1} \nop2={op2}')
                    print()
                    partial_set.add(op1 + op2)
                    partial_set.add(op1 * op2)
                    partial_set.add(op1 - op2)
                    if op2 != 0:
                        partial_set.add(op1 // op2)
        if number in partial_set:
            return cnt
        set_list.append(partial_set)
    return -1

a = solution3(3, 14)
print(a)
