for x in '0123456789abcdefghijk':
    alg = int(f'7418{x}{x}461', 22) + int(f'719625{x}4', 22) + int(f'396{x}99', 22)
    if alg % 21 == 0:
        print(alg // 21)

answer = 19614415862

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1405, answer, '04ffec330b9d276c1c81c59c1d1a4376'))