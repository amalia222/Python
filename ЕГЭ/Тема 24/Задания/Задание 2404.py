line = open('Задание 2404.txt').readline()
max_len = 0
for i in '0123456789':
    line = line.replace(i, ' ')
lines = line.split()
for l in lines:
    ch = len(set(list(l)))
    if ch == 26:
        if max_len < len(l):
            max_len = len(l)

print(max_len)