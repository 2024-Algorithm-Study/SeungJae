# 백준 2468 - 안전 영역
# 실1

# 접근법
# 모든 층을 돌면서 -> for문
# 안전 영역 갯수 세고 -> bfs
# 최대 갯수 갱신 -> if

from collections import deque
from copy import copy

# 방문처리 -> map 원소 0으로 바꾸기
def bfs(floor, map):
    global N

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    safety_area = 0

    for k in range(N):
        for j in range(N):
            if map[k][j] > floor:
                deq = deque()
                deq.append([k, j])

                while deq:
                    a, b = deq.popleft()
                    map[a][b] = 0
                    
                    for ii in range(4):
                        nx = a + dx[ii]
                        ny = b + dy[ii]

                        if 0<=nx<N and 0<=ny<N and map[nx][ny] > floor:
                            deq.append([nx, ny])

                safety_area += 1

    return safety_area

if __name__ == '__main__':
    N = int(input())
    graph = []
    top = 0 # 가장 높은 높이
    most = 0 # 안전 영역 최대 개수

    for i in range(N):
        graph.append(list(map(int, input().split())))
        if max(graph[i]) > top:
            top = max(graph[i])

    for i in range(1, top+1):   
        map = [arr[:] for arr in graph]
        count = bfs(i, map)
        if count > most: # 최대 갯수 갱신
            most = count
    
    print(most)

    
    
    
