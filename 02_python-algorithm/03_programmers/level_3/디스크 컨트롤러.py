# https://school.programmers.co.kr/learn/courses/30/lessons/42627

'''
핵심
1. ((작업이 기다리는 시간 + 작업시간)의 합 / 모든 작업 수) 를 최소화
2. 현재 처리 가능한 요청 중에 가장 짧은 작업시간을 우선 처리 -> 기다리는 시간 최소화
3. jobs를 요청 시간 순으로 정렬 -> 시작한 작업의 걸리는 시간 - 요청시간 > 0 -> 힙에 삽입
4. 우선순위 정렬은 짧은 작업시간으로 한다.
5. 작업이 끝나면 -> 힙의 heappop으로 작업 시작
6. 반복

필요한 변수
- ongoing_work = [] <- 현재 진행중인 작업의 정보
- next_work = []  <- 진행중인 작업 외 나머지 작업 중에 가장 짧은 작업 시간
- sum = 0  <- 각 작업별 요청부터 종료까지 소요시간
- 
'''

def solution(jobs):
    answer = 0
    return answer