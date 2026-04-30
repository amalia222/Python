def f(x, y, s):
    if (x + 2) > y:
        return 0
    if x == y:
         return 1
    if s < 1:
        return f(x - 1, y, s + 1) + f(x + 3, y, 0) + f(x * 2, y, 0)
    else:
        return f(x + 3, y, 0) + f(x * 2, y, 0)

print(f(3, 12, 0))

answer = 53

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(23, 2304, answer, 'd82c8d1619ad8176d665453cfb2e55f0'))