# 백준 10799 - 쇠막대기

stick = input()

def solution(stick):
    answer = 0
    stack = []
    pre = '('

    for i in stick:
        if i == '(':
            stack.append('(')
        else:
            if pre == '(':
                stack.pop()
                answer += len(stack)
            else:
                stack.pop()
                answer += 1
        
        pre = i   
    return answer

print(solution(stick))