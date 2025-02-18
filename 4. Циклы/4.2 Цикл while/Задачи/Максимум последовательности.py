el = int(input())
n = el
pos_max = 0
el_sum = 1
while el != 0:
    if pos_max < n:
        pos_max = el
        if el_sum < n:
            el_sum = 1
    elif n == pos_max and not pos_max > n:
        el_sum += 1
    el = int(input())
print(el_sum, n)