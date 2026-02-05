from sys import setrecursionlimit
setrecursionlimit(5000)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1)

print((f(2024) - f(2023)) // f(2022))
answer = 4092529

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1610, answer, 'e8b6b9482031792df830fa44bfbeda43'))