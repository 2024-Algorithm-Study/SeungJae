# 백준 2667 - 단지번호붙이기
# 실1

def dfs(x, y):
    global home
    if x < 0 or y < 0 or x >= N or y >= N:
        return False

    if arr[x][y] == 1:
        home += 1
        arr[x][y] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False


if __name__ == "__main__":
    N = int(input())
    arr = []

    for i in range(N):
        arr.append(list(map(int,input())))

    home = 0
    count = []

    for x in range(N):
        for y in range(N):
            if dfs(x, y):
                count.append(home)
                home = 0
                
    count.sort()

    print(len(count))
    for i in count:
        print(i)


   




