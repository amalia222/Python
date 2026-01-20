from itertools import *
list_val = list(product('0123456789ABCDEF', repeat = 6))
count = 0
for i in list_val:
    i = ''.join(i)
    if i.count('5') >= 1:
        if i.count('CC') == 1 or i.count('DD') == 1 or i.count('EE') == 1 or i.count('FF') == 1:
            count += 1
print(count)
answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 84, answer, '85705f54f8b912d25a2eac2583e7093d'))