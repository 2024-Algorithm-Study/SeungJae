# 백준 2606 - 바이러스
# 실3

def virus(V):
    global arr, N, visited

    visited[V] = 1
    
    for i in range(1, N+1):
        if arr[V][i]==1 and visited[i]==0:
            arr[V][i] = 0
            arr[i][V] = 0

            virus(i)


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    arr = [[0]*(N+1) for _ in range(N+1)]
    visited = [0]*(N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1
    
    virus(1)

    print(sum(visited)-1)