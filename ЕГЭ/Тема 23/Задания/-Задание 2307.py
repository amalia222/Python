def f(x, y, k3, k4):
    if x == y:
        return 1
    if x > y or k3 + k4 > 1:
        return 0
    return f(x + 1, y, k3, k4) + f(x + 2, y, k3, 4) + f(x * 2, y, k3 + 1, k4) + f(x * 3, y, k3, k4 + 1)
print(f(1, 10, 0, 0))
answer = 19

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(23, 2307, answer, '26657d5ff9020d2abefe558796b99584'))