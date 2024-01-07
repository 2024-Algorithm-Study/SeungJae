cost = int(input())

exchange = 1000 - cost
count = 0
exchange_list = [500, 100, 50, 10, 5, 1]

for i in exchange_list:
    count += exchange // i
    exchange %= i

print(count)
