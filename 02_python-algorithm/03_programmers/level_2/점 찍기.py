import math

def solution(k, d):
    answer = 0
    for x in range(0, d+1, k):
        y = (d*d - x*x)**0.5
        answer += int(y // k) + 1
    return answer
  
answer = solution(1, 5)
print(answer)

'''
이중 포문을 했을 때 시간초과 발생함.
한 좌표를 기준으로 피타고라스 정리를 이용 yy = dd - xx
최대 길이의 한 좌표가 나왔을 때 거기에 k를 나눈 몫이 좌표의 개수 인데 1개씩 더해야함.
1을 더하는 이유는 y가 0인 x축 좌표들을 추가한 것
'''

def solution1(k, d):
    c = 0
    for y in range(0, d, k):
        x = (d**2 - y**2)**0.5
        c += x//k
    return c + d//k + 1