for a in range(1, 100):
    if all((3 * x + 7 * y < a) or (x >= y) or (y > 6) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
answer = 58

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(15, 1505, answer, '66f041e16a60928b05a7e228a89c3799'))