from itertools import *
list_val = list(product('АКОРСТ', repeat = 5))
max_index = 0
for i in range(len(list_val)):
    if i % 2 == 0:
        s = ''.join(list_val[i])
        if s.count('О') == 2:
            if s[0] !='А' and s[0] !='С' and s[0] !='Т':
                if i > max_index:
                    max_index = i
print(max_index)
answer = 5162

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 82, answer, '7ffb4e0ece07869880d51662a2234143'))