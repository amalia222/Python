# Решение
'''
def alg_51(n):
    binary = bin(n)[2:]
    binary += bin(n % 3)[2:].zfill(2)
    b_dig = int(binary, 2)
    binary += bin(b_dig % 5)[2:].zfill(3)
    return int(binary, 2)

count = 0
n = 34722223

while n <= 45138888:
    for i in range(1111111110, 1444444417):
        if alg_51(n) == i:
            count += 1
    n += 1
'''
answer = 10416665

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 51, answer, '389499b02f30212486e408cd73a5bc50'))