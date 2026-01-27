'''def f(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return f(n - 1) + 2 * n - 1
    else:
        return 4 * f(n // 2)
n = 448369
print(f(n))'''
for x in range(1, 1000):
    for y in range(1, 1000):
        if x ** 2 - y ** 2 == 1001:
            print(x - y)
answer = 13

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1609, answer, 'c51ce410c124a10e0db5e4b97fc2af39'))