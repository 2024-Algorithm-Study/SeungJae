# 백준 1260 - DFS와 BFS
# 실2

from collections import deque
import copy

def dfs(V):
    global visited, arr, answer, N

    visited[V] = 1
    answer.append(V)

    for i in range(1, N+1):
        if arr[V][i] == 1 and visited[i] == 0:
            arr[V][i] = 0
            arr[i][V] = 0
            dfs(i)


def bfs(V):
    global answer_bfs, N, arr_bfs
    deq = deque([V])
    visited_bfs = [0] * (N+1)
    
    while deq:
        visited_bfs[deq[0]] = 1
        for i in range(1, N+1):
            if arr_bfs[deq[0]][i] == 1 and visited_bfs[i] == 0:
                deq.append(i)
                visited_bfs[i] = 1
        answer_bfs.append(deq.popleft())


if __name__ == "__main__":
    N, M, V = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    answer = []
    answer_bfs = []

    for _ in range(M):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1
    
    arr_bfs = copy.deepcopy(arr)

    dfs(V)
    bfs(V)

    print(*answer)
    print(*answer_bfs)

    