'''
콜라츠 추측, 우박수열

1-1. 입력된 수가 짝수라면 2로 나눕니다.
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
2.결과로 나온 수가 1보다 크다면 1번 작업을 반복합니다.

초항이 K인 우박수열
x = 0일때 y = K이고
다음 우박수는 x = 1에 표시해서 그래프 만듬


은지는 이렇게 만든 꺾은선 그래프를 정적분 해보고 싶어졌습니다.
x에 대한 어떤 범위 [a, b]
[a, b]에 대한 정적분 결과는 꺾은선 그래프와 x = a, x = b, y = 0 으로 둘러 쌓인 공간의 면적과 같습니다. 
이것을 우박수열 정적분

구간의 시작은 음이 아닌 정수
구간의 끝은 양이 아닌 정수
각각 꺾은선 그래프가 시작하는 점과 끝나는 점의 x좌표에 대한 상대적인 오프셋을 의미

[0,0] 구간에 대해 정적분 한다면 전체 구간에 대한 정적분
[1,-2] 구간에 대해 정적분 한다면 1 ≤ x ≤ 3인 구간에 대한 정적분


우박수의 초항 k, 정적분을 구하는 구간들의 목록 ranges
정적분의 결과 목록을 return

단, 주어진 구간의 시작점이 끝점보다 커서 유효하지 않은 구간이 주어질 수 있으며 이때의 정적분 결과는 -1로 정의
'''

def solution(k, ranges):
    result = []
    collatz = [k]
    integral = []
    count = 0
    
    while k != 1:
        if k % 2 == 0:
            k = k / 2
        else:
            k = k * 3 + 1
        collatz.append(k)
        count += 1
        
    for i in range(0, len(collatz)):
        integral.append((collatz[i] + collatz[i + 1]) / 2)
    
    