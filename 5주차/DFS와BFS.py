# 백준 1260 - DFS와 BFS
# 실2

def dfs(V):
    global visited, arr, answer, N

    visited[V] = 1
    answer.append(V)

    for i in range(1, N+1):
        if arr[V][i] == 1 and visited[i] == 0:
            arr[V][i] = 0
            arr[i][V] = 0
            dfs(i)

if __name__ == "__main__":
    N, M, V = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    answer = []

    for _ in range(M):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1

    dfs(V)

    print(*answer)

    