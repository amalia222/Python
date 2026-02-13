x = 343 ** 5 + 343 ** 4 + 49 ** 6 - 7 ** 13 - 21
del7 = ''
while x != 0:
    del7 += str(x % 7)
    x //= 7
alg = len(set(list(del7[::-1])))
print(del7)
print(alg)

answer = 4

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1407, answer, 'a87ff679a2f3e71d9181a67b7542122c'))