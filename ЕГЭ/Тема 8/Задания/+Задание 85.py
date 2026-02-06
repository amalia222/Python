from itertools import *

list_val = list(product('АГМНСТУ', repeat = 6))

for i in range(len(list_val) - 1, 1, -1):
    s = ''.join(list_val[i])
    if s[0] != 'У':
        if s.count('М') == 2 and s.count('Г') <= 1:
            print(i)
            break
print(len(list_val))
answer = 100810

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 85, answer, '4f41663a6f277ab55c6b626aff28784a'))