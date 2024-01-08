def solution(n, lost, reserve):
    answer = 0
    
    lost.sort()
    reserve.sort()
    
    # # [:] 복사본에 대해 반복을 수행하기 때문에 reserve의 원소를 삭제할 경우 반복에 문제 없음
    # for i in reserve[:]:
    #     if i in lost:
    #         reserve.remove(i)
    #         lost.remove(i)
    
    for i in reserve[:]:
        if i-1 in lost:
            lost.remove(i-1)   
        elif i in lost:
            lost.remove(i)
        elif i+1 in lost:
            lost.remove(i+1)
            
    return n - len(lost)