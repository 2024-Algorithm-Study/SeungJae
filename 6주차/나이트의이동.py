# 백준 7562 - 나이트의 이동
# 실1

# TIP
# 모든 경우를 동시에 카운트해가다가 정답 발견하면 카운트 출력 후 stop
# => DFS보다 BFS 적합 문제
# => DFS로 답을 찾으려면 엄청 오래걸리기에 DFS는 적합하지 않음

from collections import deque

def knight(a, b):
    global x2, y2, l, dx, dy, graph
    deq = deque()
    deq.append([a, b])

    while deq:
        x, y = deq.popleft()
        graph[x][y] = 1

        if x==x2 and y==y2:
            return graph[x2][y2]

        for i in range(8):
            mx = x + dx[i]
            my = y + dy[i]

            if ((0<=mx and mx<l) and (0<=my and my<l)) and graph[mx][my] == 0:
                graph[mx][my] = graph[x][y] + 1
                deq.append([mx, my])
    return -1



if __name__ == '__main__':
    T = int(input())
    dx = [1, 1, 2, 2, -1, -1, -2, -2]
    dy = [2, -2, 1, -1, 2, -2, 1, -1]

    for _ in range(T):
        l = int(input())
        x1, y1 = map(int, input().split())
        x2, y2 = map(int, input().split())
        graph  = [[0]*l for _ in range(l)]
        print(knight(x1, y1))
