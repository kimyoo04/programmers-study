'''
두조각 잘라 동생과 나눠먹음
여러가지 토핑 일렬로 있음
-> 동일한 토핑이 올라가면 공평하게 롤케이크가 나눠진 것으로 생각
ex - 롤케이크 4가지 종류의 토핑 올려짐 => 1,2,3,4로 표시 => [1,2,1,3,1,4,1,2] 순서로 올려져 있다.

카운트 = 0 초기화를 먼저 한다 -> 반복하여 인덱스 i, i+1 사이를 한번씩 잘라본다 -> 자른 결과 2가지를 set으로 중복을 제거한다. -> 길이를 체크해서 2가지가 같으면 카운트 +1 한다
'''

from collections import Counter

def solution(topping):
    dic = Counter(topping) # Counter 객체 활용
    dic_set = set() # 중복 제거용 set자료형 초기화
    res = 0 # 카운팅할 변수 초기화

    for i in topping:
        dic[i] -= 1
        dic_set.add(i)
        
        if dic[i] == 0:
            dic.pop(i)
        
        if len(dic) == len(dic_set):
            res += 1
            
    return res
  
answer = solution([1, 2, 1, 3, 1, 4, 1, 2])
print(answer)