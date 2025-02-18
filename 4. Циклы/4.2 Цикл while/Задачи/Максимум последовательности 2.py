el = int(input())
n = el
pos_max = 0
max_n = n
while el != 0:
    if el > n:
        n = el
        pos_max += 1
    elif el > max_n:
        max_n = el
    el = int(input())
print(pos_max, max_n)