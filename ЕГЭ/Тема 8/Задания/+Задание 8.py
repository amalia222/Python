# Решение
from itertools import *
list_val = list(product('ГЕПАРД', repeat = 5))
count = 0
for i in list_val:
    if i[0] != 'А' and i[-1] != 'Е' and i.count('Г') == 1:
        count += 1
print(count)

answer = 2200

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 8, answer, '5249ee8e0cff02ad6b4cc0ee0e50b7d1'))