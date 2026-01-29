'''def alg(n):
    bin_n = bin(n)[2:] + bin(n % 4)[2:]
    return int(bin_n, 2)
count = 0
n = 500000000
while n <= 1000000000:
    if 1_000_000_000 <= alg(n) <= 1_789_456_123:
        count += 1
    n += 1
print(count)'''
answer = 197364032

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 54, answer, '473b677ddfbedbb3d2e6d5e5980dc6e1'))