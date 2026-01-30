def alg(n):
    del2 = sum([int(x) for x in str(n) if int(x) % 2 == 0])
    del1 = sum([int(x) for x in str(n)[1::2]])
    return abs(del1 - del2)
n = 4
while True:
    if alg(n) == 13:
        print(n)
        break
    n += 1
answer = 618

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 58, answer, 'eb6fdc36b281b7d5eabf33396c2683a2'))