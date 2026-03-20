alg = 4 * 625 ** 9 - 25 ** 15 + 2 * 5 ** 11 - 7
count = 0
while alg != 0:
    if alg % 5 == 4:
        count += 1
    alg //= 5
print(count)
answer = 15

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1408, answer, '9bf31c7ff062936a96d3c8bd1f8f2ff3'))