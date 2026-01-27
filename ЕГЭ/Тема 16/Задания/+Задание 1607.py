def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 4 < 2:
        return f(n // 4) + n % 4
    else:
        return f(n // 4) + n % 4 - 1

'''n = 200243450
print(f(n), f(n + 1))
while True:
    if f(n) == 27 and f(n + 1) == 16:
        print(n)
        break
    n += 1'''
answer = 268431359

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1607, answer, '2a0b3b7b30d11559c931dde71e179f16'))