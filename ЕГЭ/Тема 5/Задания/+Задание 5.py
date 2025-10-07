# Решение

def alg(n):
    binary = bin(n)[2:]
    rev = ''.join(['1' if bit == '0' else '0' for bit in binary])
    rev = rev.lstrip('0')
    if not rev:
        rev_des = 0
    else:
        rev_des = int(rev, 2)
    return n - rev_des

n = 1
while True:
    if alg(n) == 999:
        print(n)
        break
    n += 1

answer = 1011

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 5, answer, '7f975a56c761db6506eca0b37ce6ec87'))