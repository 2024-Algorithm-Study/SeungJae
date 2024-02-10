# 6주차 - BFS

### BFS - Breadth-First Search

- 너비 우선 탐색 
- 큐 자료구조 이용
- 반복 o, 재귀 x

<br>

**동작과정**


    1. 탐색 시작 노드를 큐에 삽입 후 방문 처리

    2. 큐에서 노드를 꺼낸 뒤 해당 노드의 인접 노드 중 방문하지 않은 노드 모두 큐에 삽입 후 방문 처리

    3. 2번 반복

<br>

**코드 구현**

```python
def bfs(V):
    global visited
    queue = deque([start])
    visited[V] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [[0]*N for _ in range(N)]
visited = [False] * (N+1)
```
<br>

