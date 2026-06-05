from itertools import *
list_val = list(product('0123456789ABCDEF', repeat = 6))
count = 0
for i in list_val:
    i = ''.join(i)
    i = i.replace('D', '*').replace('E', '*').replace('F', '*')
    if i.count('5') >= 1 and i[0] != '0':
        if i.count('*') == 2 and '**' in i:
            count += 1
print(count)
answer = 335241


#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 84, answer, '85705f54f8b912d25a2eac2583e7093d'))