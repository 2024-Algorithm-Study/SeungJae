# 백준 4779 - 칸토어 집합
# 실3
import itertools


while True:
    arr = list(map(int, input().split()))

    # 0이 입력되면 종료
    if arr[0] == 0:
        break
    
    number = arr[1:]
    possible = list(itertools.combinations(number, 6))

    for tuple in possible:
        print(*tuple)
    print()


