# **idea**
# 1. 그리디 알고리즘을 사용하기 위해서 회의 시간이 짧은 회의들의 정렬 정보가 필요
# - 회의 종료 시간의 정렬을 통하여 위 문제를 해결
# - 회의 종료 시간이 같은 경우 회의 시작 시간 정렬

n = int(input())

schedule = [[0, 0] for _ in range(n)]

for i in range(n):
    schedule[i][0], schedule[i][1] = map(int, input().split())

schedule.sort(key = lambda x : (x[1], x[0]))

count = 0
end_time = -1

for time in schedule:
    if end_time == -1:
        end_time = time[1]
        count += 1
    elif end_time <= time[0]:
        end_time = time[1]
        count += 1

print(count)