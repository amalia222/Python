el = int(input())
max_value = el
i = 0
while el != 0:
    if el > max_value:
        max_value = el
        i = 1
    elif max_value == el:
        i += 1
    el = int(input())
print(i)