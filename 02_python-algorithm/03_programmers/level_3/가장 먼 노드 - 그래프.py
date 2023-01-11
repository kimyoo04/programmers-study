# https://school.programmers.co.kr/learn/courses/30/lessons/49189

'''
문제
n = 노드 개수
vertex = 간선 정보가 있는 2차원 배열

-> 가장 먼 노드의 개수 구하기
'''

'''
핵심
- vertex(edge)를 그래프 자료구조로 변환 필요
- 최단경로 -> BFS
- 방문한 노드를 인식 및 거리를 추가하기 visited 대신 distance
- False대신 -1 사용 및 한 번의 사이클마다 +1
'''

from collections import deque

def solution(n, vertex):
    answer = 0
    distance = [-1] * (n + 1)

    graph = [[] for _ in range(n + 1)]
    for node in vertex:
        graph[node[0]].append(node[1])
        graph[node[1]].append(node[0])

    queue = deque([1])
    distance[1] = 0

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if distance[i] == -1:
                distance[i] = distance[node] + 1
                queue.append(i)

    max_ = max(distance)
    for d in distance:
        if d == max_:
            answer += 1

    return answer