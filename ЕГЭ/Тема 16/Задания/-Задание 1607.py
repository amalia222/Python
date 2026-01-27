def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 4 < 2:
        return f(n // 4) + n % 4
    else:
        return f(n // 4) + n % 4 - 1

n = 1000000000
print(f(n))
while True:
    if f(n) == 27 and f(n + 1) == 16:
        print(n)
        break
    n += 1
answer = 1002434559

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1607, answer, '2a0b3b7b30d11559c931dde71e179f16'))