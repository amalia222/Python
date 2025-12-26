from itertools import *
list_val = list(product('АКОРСТ', repeat = 5))
max_index = 0
for i in list_val:
  if list_val.index(i) % 2 == 0:
    curr_index = list_val.index(i)
    i = ''.join(i)
    if i.count('О') == 2:
      if i[0] not in 'АСТ':
        max_index = curr_index
print(max_index)
print(list_val[5184])
print(list_val[5184])