from sys import setrecursionlimit
setrecursionlimit(20000)
def g(n):
    if n <= 9:
        return n * 3
    else:
        return g(n - 4) + 2

def f(n):
    return g(n - 1) + g(n - 3)

print(f(42999))
answer = 43032

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1608, answer, '0a44140fcbbf55d76a1dc8953ebecd1b'))