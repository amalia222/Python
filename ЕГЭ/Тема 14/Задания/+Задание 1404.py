for x in range(37):
    for y in range(37):
        alg = 7 * 37 ** 0 + y * 37 ** 1 + 3 * 37 ** 2 + 4 * 37 ** 3 + 6 * 37 ** 4 + x * 37 ** 5 + 2 * 37 ** 6 + 1 * 37 ** 7
        if alg % 36 == 0:
            print(x * 37 ** 0 + y * 37 ** 1)
answer = 1345

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1404, answer, '86109d400f0ed29e840b47ed72777c84'))