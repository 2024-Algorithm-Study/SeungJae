# 백준 1388 - 바닥 장식
# 실4

# DFS로 접근

def right(x, y):
    global graph, count, M, sum
    
    if y <= M-2:
        if graph[x][y+1] == '-':
            count -= 1
            graph[x][y] = 0
            if y < M-2:
                right(x, y+1)

def down(x, y):
    global graph, count, N, sum
    
    if x <= N-2:
        if graph[x+1][y] == '|':
            count -= 1
            graph[x][y] = 0
            if x < N-2:
                down(x+1, y)


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = []
    
    for _ in range(N):
        graph.append(list(input()))
    
    count = N*M
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == '-':
                right(i, j)
                
            elif graph[i][j] == '|':
                down(i, j)      

    print(count)