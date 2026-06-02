def is_simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True

def get_del(n):
    s = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            s.append(i)
            n //= i
    if n > 1:
        s.append(n)
    return max(s) if len(s) == 2 and all(str(x).count('3') == 2 for x in s) else False

for i in range(8996452, 9050000):
    get_deli = get_del(i)
    if get_deli:
        print(i, get_deli)
# Ответ в виде списка чисел []
# 1й столбец
answer1 = [9001609, 9002887, 9006149, 9012167, 9012373]
# 2й столбец
answer2 = [24133, 38639, 38653, 3853, 23531]

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(25, 2505, answer1 + answer2, '00d6c721eebbe5dc2db2b6b3e34e9a83'))