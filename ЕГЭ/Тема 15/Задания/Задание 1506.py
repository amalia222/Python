p = range(167242, 514210)
q = range(403149, 718530)
r = range(522897, 816282)
s = []
for x in range(167242, 816282):
    for y in range(x + 1, 816282 + 1):
        a = range(x, y)
        if all((i in q) <= (((i in p) or (i in r)) <= (i in a)) for i in range(1, 100)):
            s.append(len(a))
            print(len(a))
print(min(s))
answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(15, 1506, answer, 'e0ee0001e619cc4b3b2113d235f9416f'))