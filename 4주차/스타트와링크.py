# 백준 14889 - 스타트와 링크
# 실1

# 조합 사용
# -> itertools.combinations

import itertools

N = int(input())

def startlink(N):
    player = [i for i in range(1, N+1)]
    # 2차원 배열 만들기
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    # 가능한 팀 조합 리스트
    possible_team = list(itertools.combinations(player, N//2))

    distance = 100

    for i in possible_team:
        # 각 팀에서 모든 두명 조합 리스트
        possible_a = list(itertools.combinations(list(i), 2))
        possibla_b = list(itertools.combinations(list(set(player) - set(list(i))), 2))
        sum_a, sum_b = 0, 0

        # 만들어둔 2차원 배열 이용하여 총 합 점수 구하기
        for mem in possible_a:
            sum_a += (arr[mem[0]-1][mem[1]-1] + arr[mem[1]-1][mem[0]-1])
        
        for mem in possibla_b:
            sum_b += (arr[mem[0]-1][mem[1]-1] + arr[mem[1]-1][mem[0]-1])
        
        if abs(sum_a - sum_b) < distance:
            distance = abs(sum_a - sum_b)
    
    return distance

print(startlink(N))




