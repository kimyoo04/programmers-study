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

def solution1(n, vertex):
    answer = 0
    distance = [-1] * (n + 1)

    # 인접 리스트 표현
    graph = [[] for _ in range(n + 1)]
    for node in vertex:
        graph[node[0]].append(node[1])
        graph[node[1]].append(node[0])

    # 출발 노드 설정
    queue = deque([1])

    # 거리 노드 설정
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


# A* 알고리즘으로 풀어보기 --> 가능하지만 비효율
# 이유는 목적지가 한개가 아니기 때문임. 변하는 목적지 사이의 거리를 전부 기억해야함.

'''
http://www.gisdeveloper.co.kr/?p=3897
https://choiseokwon.tistory.com/210

A-Star는 휴리스틱 함수에 기반해서
주어진 꼭짓점(노드)마다 최단 경로임을 판단한 후
이동하는 그래프 탐색 알고리즘

- 시간복잡도는 휴리스틱 함수에 따라 달라진다.
- heapq를 사용하여 H의 최소값을 pop 시킨다.
-

F - 출발지에서 목적지까지의 값
G - 현재 위치에서 출발지까지의 값
H - 현재 위치에서 목적지까지의 값

F = G + H

opened_list와 closed_list로 분리해서 확인하며

parent node 를 기억하고 있어 최종 목적지에 도달했을 때
parent node 를 따라 경로를 역으로 따라가서 찾는다.
'''

a = solution1(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
print(a)