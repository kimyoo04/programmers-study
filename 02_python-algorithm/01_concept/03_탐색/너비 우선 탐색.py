from collections import deque

# BFS
def bfs(graph, start):
    visited = [False]*(len(graph))
    queue = deque([start]) # 큐 구현

    visited[start] = True # 시작 노드 방문 처리

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 꺼내서 출력
        node = queue.popleft()
        print(node, end=' ')

        # 꺼낸 원소와 인접노드 확인
        for i in graph[node]:
            # 아직 방문하지 않은 노드라면
            if not visited[i]:
                queue.append(i)
                visited[i]=True
