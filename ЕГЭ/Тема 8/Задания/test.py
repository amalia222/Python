from itertools import *
list_val = product('ВЕРОНИКА', repeat = 6)
count = 0
for s in list_val:
    if s.count('Е') + s.count('О') + s.count('И') + s.count('А') > s.count('В') + s.count('Р') + s.count('Н') + s.count('К'):
        count += 1
print(count)
