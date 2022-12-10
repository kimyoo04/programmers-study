'''
내림차순으로 순서대로 되는 개수까지 카운트하기
'''

def solution(order):
    order.reverse()
    belt = list(range(len(order), 0, -1)) # 내림차순 리스트 생성
    sub_belt = []
    count = 0
    while True:
        # 
        if belt and order and order[-1] == belt[-1]:
            order.pop()
            belt.pop()
            count += 1
        elif sub_belt and order and order[-1] == sub_belt[-1]:
            order.pop()
            sub_belt.pop()
            count += 1
        elif belt:
            sub_belt.append(belt.pop())
        else:
            break
    return count
  

# stacks 사용
def solution1(order):
    stacks_belt = []
    N = len(order)
    i = 1
    idx = 0
    
    while i < N+1:
        stacks_belt.append(i)
        # print(stacks_belt, idx, i)

        while stacks_belt[-1] == order[idx]:
            idx += 1
            stacks_belt.pop()
            if len(stacks_belt) == 0:
                break
              
        i += 1

    return idx

a = solution1([4, 3, 1, 2, 5])
print(a)

