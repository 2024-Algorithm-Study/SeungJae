X = int(input())

def search(X):
    step = 1 # 2 3 4 5 6
    count = 0 # 1 3 6 10 15
    for i in range(1, 10000000):
        count += i
        step += 1

        if X <= count and X > (count-i):
            break
    
    if step % 2 == 0:
        return str(count-X+1) + '/' + str(step-(count-X+1))
    elif step % 2 == 1:
        return str(step-(count-X+1)) + '/' + str(count-X+1)
         
print(search(X))