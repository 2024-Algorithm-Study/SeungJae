# 백준 4779 - 칸토어 집합
# 실 3

def cantore(start, N):
    if N == 1:
        return
    
    for i in range(start + N//3, start + (N//3)*2):
        result[i] = ' '

    cantore(start, N//3)
    cantore(start + N//3*2, N//3)

while True:
    try:
        N = int(input())
        result = ['-' for i in range(3**N)]
        cantore(0, 3**N)
        print(''.join(result))
    except:
        break

