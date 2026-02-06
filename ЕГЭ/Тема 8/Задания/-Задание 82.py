from itertools import *
list_val = list(product('АКОРСТ', repeat = 5))
max_index = 0
for i in range(len(list_val)):
    if (i + 1) % 2 == 0:
        s = ''.join(list_val[i])
        if s.count('О') == 2:
            if s[0] !='А' and s[0] !='С' and s[0] !='Т':
                max_index = i
print(max_index + 1)

answer = 5058