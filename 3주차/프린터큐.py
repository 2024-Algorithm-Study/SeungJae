# 백준 1966 - 프린터 큐
from collections import deque

T = int(input())

def printer(T):
    answer = []

    for _ in range(T):
        N, M = map(int, input().split())
        deq_count = deque()
        deq_imp = deque()
        count = 1
        
        lst = list(map(int, input().split()))

        for i, j in enumerate(lst):
            deq_imp.append(j)
            deq_count.append(i)

        while True:
            check = False
            for i in range(0, len(deq_imp)):
                if deq_imp[0] < deq_imp[i]:
                    check = True
                    break
            
            if check :
                deq_imp.append(deq_imp.popleft())
                deq_count.append(deq_count.popleft())
            else:
                if deq_count[0] == M:
                    answer.append(count)
                    break
                else:
                    deq_imp.popleft()
                    deq_count.popleft()
                    count += 1
    
    return answer

for i in printer(T):
    print(i)


                    


        
        

        

    






