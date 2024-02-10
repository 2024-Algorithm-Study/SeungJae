# 백준 7576 - 토마토
# 골5

# idea
# 모든 1 위치 에서 동시에 dfs 시작 - 동시에 하루에 한번씩 재귀
# graph에서 0이 사라지는 순간 stop - 0 체크 함수 따로 빼서 함수 종료조건 만들기

# 날짜가 1,000*1,000이 넘어가면 -1 출력
# 

def zero_check(graph):
    for i in graph:
        if 0 in i:
            return True
        return False
    

def tomato()

if __name__ == "__main__":
    M, N = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]





