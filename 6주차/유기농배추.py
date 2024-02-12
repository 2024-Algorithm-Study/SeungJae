# 유기농 배추 - 1012
# 실2


# 재귀 깊이 제한 두기
# 백준 기본 1000
import sys
sys.setrecursionlimit(10000)

def dfs(a, b):
    global graph, M, N, count

    if a<0 or b<0 or a>=N or b>=M:
        return

    if graph[a][b] == 0:
        return
    
    count += 1
    graph[a][b] = 0

    dfs(a-1, b) # 좌
    dfs(a+1, b) # 우
    dfs(a, b+1) # 상
    dfs(a, b-1) # 하

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        M, N, K = map(int, input().split())
        graph = [[0]*M for _ in range(N)]
        answer = 0

        for _ in range(K):
            a, b = map(int, input().split())
            graph[b][a] = 1

        for i in range(N):
            for j in range(M):
                count = 0
                dfs(i, j)
                if count > 0:
                    answer += 1
        
        print(answer)

    