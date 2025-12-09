list_val = [int(c) for c in open('Пример 2.txt')]
min3 = min(list_val) % 3
max7 = max(list_val) % 7
res_count = 0
res_max = 0
for i in range(len(list_val) - 2):
    triple = list_val[i:i + 3]
    i3 = [j for j in triple if j % 3 == min3]
    i7 = [j for j in triple if j % 7 == max7]
    if len(i3) == 1 and len(i7) >= 2:
        res_count += 1
        if res_max < sum(triple):
            res_max = sum(triple)
print(res_count, res_max)