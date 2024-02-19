# 백준 2178 - 미로 탐색
# 실1

# 최단거리 --> BFS

from collections import deque

def bfs(a, b):
    global N, M, graph

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    deq = deque()
    deq.append([a, b])

    while deq:
        x, y = deq.popleft()

        if x == N-1 and y == M-1:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                deq.append([nx, ny])


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = []
    
    for _ in range(N):
        graph.append(list(map(int, input())))

    bfs(0, 0)

    print(graph[N-1][M-1])
    
    