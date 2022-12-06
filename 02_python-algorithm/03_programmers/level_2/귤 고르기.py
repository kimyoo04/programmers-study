from collections import Counter

def solution(k, tangerine):
    answer = 0
    sum = 0
    tan = Counter(tangerine).most_common()
    
    for t in tan:
        sum += t[1]
        answer += 1
        if sum >= k:
            return answer
  
answer = solution(6, [1, 3, 2, 5, 4, 5, 2, 3])
print(answer)

'''
- 각 무게별 귤의 개수를 구하기 (Counter 사용)
- 내림차순 정렬하기
- k개를 선택할 때까지 순서대로 더하기
'''



def solution1(k, tangerine):
    answer = 0
    length=len(tangerine)
    dict={}

    for i in tangerine:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1

    arr=sorted(dict.items(), key=lambda item: -item[1])

    total=0
    for item in arr:
        total+=item[1]
        answer+=1
        if(total>=k):
            break

    return answer