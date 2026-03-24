for x in range(7):
    alg = str(4 * 7 ** 24 + 6 * 7 ** 13 + 5 * 49 ** 4 + 2 * 343 ** 2 + 10 - x)
    if alg.count('6') > alg.count('0'):
        print(x)

answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1409, answer, '6fe07c291b01e40ad858b4d56aa3f33e'))