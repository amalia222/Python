min_val = 10 ** 10
for x in '0123456789ABC':
    for y in '0123456789ABC':
        alg = int(f'8{x}78{y}', 13) + int(f'79{x}{y}7', 18)
        if alg % 9 == 0 and alg < min_val:
            min_val = alg
            print(x, y, alg // 9)

answer = 113024

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1401, answer, '436fc6a87245490c1c09148823eec9ff'))