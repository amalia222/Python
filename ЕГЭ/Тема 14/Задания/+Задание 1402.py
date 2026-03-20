for x in '0123456':
    for y in range(7):
        alg = int(f'{y}{x}320', 7) + int(f'1{x}3{y}3', 9)
        if alg % 181 == 0:
            print(x, y, alg // 181)
answer = 148

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1402, answer, '47d1e990583c9c67424d369f3414728e'))