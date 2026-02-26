def f(x, y, k = 0):
    if x == y:
        return 1
    if x > y or k > 2:
        return 0
    return f(x + 1, y, k) + f(x + 2, y, k) + f(x * 2, y, k + 1) + f(x * 3, y, k + 1)

print(f(1, 10))
answer = 196

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(23, 2307, answer, '26657d5ff9020d2abefe558796b99584'))