# 5주차 - DFS

### DFS - Depth-First Search

- 깊이 우선 탐색 
- 스택 자료구조와 재귀 함수 이용

<br>

**동작과정**


    1. 탐색 시작 노드를 스택에 삽입 후 방문 처리

    2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 스택에 넣고 방문 처리. 방문하지 않은 인접 노드가 없다면 최상단 노드 꺼내기

    3. 1, 2번 재귀

<br>

**코드 구현**

```python
def dfs(v):
    global visited
    visited[idx] = True
    print(idx, end=' ')
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)

graph = [[0]*N for _ in range(N)]
visited = [False] * N
```
<br>

**Tip**
- 방문 처리 배열 -> visited
- 그래프 -> 2차원 배열

    




