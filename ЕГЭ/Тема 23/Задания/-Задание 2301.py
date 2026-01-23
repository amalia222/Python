def f1(x, y):
    if y == x:
        return 1
    if x > y or x == 27:
        return 0
    return f1(x + 1, y) + f1(x * 2, y) + f1(x * 3, y)

def f2(x, y):
    if y == x:
        return 1
    if x > y or x == 24:
        return 0
    return f2(x + 1, y) + f2(x * 2, y) + f2(x * 3, y)

print((f1(9, 24) * f1(24, 81)) + (f2(9, 27) * f2(27, 81)))
answer = 62

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(23, 2301, answer, 'a8baa56554f96369ab93e4f3bb068c22'))