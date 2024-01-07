# ** idea **
# 1. 그리디 알고리즘을 사용하기 위해 위치 배열을 정렬해준다
# 2. 시작 위치를 배열의 첫번째 원소로 지정하고 for문을 돌린다
# 3. (현위치 + 0.5) 와 (시작 위치 - 0.5)의 거리가 테이프의 길이가 넘어가는지를 체크하면서
# 매 순간마다 테이프를 최대 효율로 사용하는 방법을 선택한다.

N, L = map(int, input().split())
location = list(map(int, input().split()))

def surigong(N, L, location):
    location.sort()
    start = location[0]
    count = 1
    
    for i in range(1, len(location)):
        if (location[i] + 0.5) - (start - 0.5) <= L:
            continue
        else:
            count += 1
            start = location[i]
    
    return count

print(surigong(N, L, location))