'''f = [0] * 1_000_000_000
for n in range(1000000000):
    if n == 0:
        f[0] = 0
    elif n % 2 != 0:
        f[n] = f[n - 1] + 1
    else:
        f[n] = f[n // 2]

print(f.count(2))'''
answer = 435

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1602, answer, 'ddb30680a691d157187ee1cf9e896d03'))