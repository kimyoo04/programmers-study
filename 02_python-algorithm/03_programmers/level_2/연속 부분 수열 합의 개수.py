def solution(elements):
    result = set()
    
    elementLen = len(elements)
    elements = elements * 2 # [7, 9, 1, 1, 4, 7, 9, 1, 1, 4]
    
    for i in range(elementLen):
        for j in range(elementLen):
            result.add(sum(elements[j:j+i+1]))
    return len(result)
  
a = solution([7,9,1,1,4])
print(a)

'''
원순열의 경우 리스트에 * 2를 통해서 연장한다.

이중 for문을 통해 포인터를 처음인덱스와 끝 인덱스를 얻는다. 
인덱스를 j:j+i+1을 사용해서 이중 for 문 도는 것은 처음본다!

set과 set의 메소드 add를 사용하고, len으로 정답을 구한다.
'''