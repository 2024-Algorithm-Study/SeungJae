# 안쪽부터 한겹씩 채워나가기
# => 총 N//2 겹

N = int(input())
X = int(input())

def snail(N, X):
    # N*N 리스트 생성
    arr = [[0 for i in range(N)] for i in range(N)]
    
    arr[N//2][N//2] = 1
    arr[N//2-1][N//2] = 2

    x, y = N//2, N//2
    step = 1 # 채울 숫자
    roop = 2 # 2씩 증가

    # 안쪽부터 한 겹씩 채우기
    for i in range(N//2):
        x -= 1
        step += 1
        arr[x][y] = step 

        # right   
        for i in range(roop-1):
            y += 1
            step += 1
            arr[x][y] = step

        # down
        for i in range(roop):
            x += 1
            step +=1
            arr[x][y] = step
            
        # left
        for i in range(roop):
            y -= 1
            step += 1
            arr[x][y] = step

        # up
        for i in range(roop):
            x -= 1
            step += 1
            arr[x][y] = step

        roop += 2

    return arr

arr = snail(N, X)

answer_x = 0
answer_y = 0
for i in range(N):
    for j in range(N):
        print(str(arr[i][j])+' ', end='')
        if arr[i][j] == X:
            answer_x = i+1
            answer_y = j+1
    print()

print(str(answer_x) + " " + str(answer_y))


    







    
    
    



    

    
        






