el = int(input())
max_value = el
pos_max = 0
i = 0
while el != 0:
    if el > max_value:
        max_value = el
        pos_max = i
    el = int(input())
    i += 1
print(max_value, pos_max)
