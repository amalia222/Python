def f(n):
    if n < 4000:
        return n
    if n >= 4000 and n % 7 == 0:
        return n + f(n // 7)
    else:
        return 567 + f(n - 3)

n = 4001
while True:
    if f(n) > 80000:
        print(n)
        break
    n += 1
answer = 62962

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1606, answer, 'c664ec48cfb940b2ce2386c8fb7f9be8'))