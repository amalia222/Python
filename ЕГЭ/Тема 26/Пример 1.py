f = open('Пример 1.txt')
_ = f.readline()
start_time = 0
end_time = 86400000
time = sorted(list(map(int, line.split())) for line in f.readlines())
# Сделать проще и понятнее
time.append([end_time, end_time])
max_end = 0
no_working = []
for t in time:
    if max_end >= t[0]:
        max_end = max(max_end, t[1])
    else:
        no_working.append(t[0] - max_end)
        max_end = t[1]
print(len(no_working), sum(no_working))
