for x in range(39):
    alg1 = 1 * 39 ** 0 + 7 * 39 ** 1 + x * 39 ** 3 + 3 * 39 ** 4 + 5 * 39 ** 5 + 6 * 39 ** 6
    alg2 = 7 * 39 ** 0 + 3 * 39 ** 1 + x * 39 ** 3 + 2 * 39 ** 4 + 4 * 39 ** 5
    if (alg1 + alg2) % 14 == 0:
        print((alg1 + alg2) // 14)
answer = 1566885991

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1406, answer, '288e0c30469777cb2cfd847e9fb0f529'))