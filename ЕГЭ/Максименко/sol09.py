import openpyxl
from collections import Counter
# Можно было сохранить в txt и парсить его, без использования библиотеки openpyxl
wb = openpyxl.load_workbook('09var04.xlsx')
ws = wb.active

count = 0
for row in ws.iter_rows(values_only=True):
    nums = [n for n in row if n is not None]
    if len(nums) != 4:
        continue

    c = Counter(nums)
    pairs = sum(1 for v in c.values() if v == 2)
    singles = sum(1 for v in c.values() if v == 1)
    cond1 = (pairs == 1 and singles == 2)

    if cond1:
        min_val = min(nums)
        max_val = max(nums)
        middle = [x for x in set(nums) if x != min_val and x != max_val]
        cond2 = len(middle) == 1 and middle[0] < 30
        if cond2:
            count += 1

print(count)
