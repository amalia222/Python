for a in range(1, 100):
    if not(all((x + 2 * y > 48) or (y > x) or (x + 3 * y < a) for x in range(1, 100) for y in range(1, 100))):
        print(a)
answer = 64

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(15, 1511, answer, 'ea5d2f1c4608232e07d3aa3d998e5135'))