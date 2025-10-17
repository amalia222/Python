# Решение
from itertools import product

m = len([p for p in product('1357', repeat=5) if max([p.count(x) for x in p]) <= 4])
n = len([p for p in product('2468', repeat=6) if max([p.count(x) for x in p]) <= 4])
print(2 * m * n)
answer = 8200800

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 17, answer, 'd67d496249f30f93dd6a7a6d84701d60'))