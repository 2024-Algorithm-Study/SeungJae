# 백준 9012 - 괄호

T = int(input())

def VPS(T):
    lst = []
    answer = []
    # 괄호 문자열을 한줄 씩 입력 받아 lst에 넣기
    for i in range(T):
        line = input()
        lst.append(line)
    
    for i in lst:
        stack = []
        for char in i:
            # 스택이 비어있을 떄
            if len(stack) == 0:
                if char == ')':
                    stack.append(')')
                    break
                else:
                    stack.append('(')
            # 스택이 차 있을 떄
            else:
                if char == '(':
                    stack.append('(')
                elif char == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    elif stack[-1] == ')':
                        stack.append(')')
                        break
        if len(stack) == 0:
            answer.append('YES')
        else:
            answer.append('NO')
    
    return answer

for i in VPS(T):
    print(i)


