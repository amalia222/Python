from itertools import *
list_val = list(product('АКОРСТ', repeat = 5))
for i in range(len(list_val)):
    s = ''.join(list_val[i])
    if s[0] not in 'АСТ' and s.count('О') == 2:
        print(i)

answer = 5058

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 82, answer, '7ffb4e0ece07869880d51662a2234143'))