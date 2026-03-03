from time import time
s = input()
start = time()
s_set = sorted(set(s))
s_matr = sorted(list(s))
for i in s_set:
    s_matr.remove(i)
print(*s_matr)
end = time()
print(end - start)

answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(15, 1508, answer, 'f7177163c833dff4b38fc8d2872f1ec6'))