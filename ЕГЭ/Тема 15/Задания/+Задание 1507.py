p = range(17, 54)
q = range(37, 83)
s = []
for start in range(10, 90):
    for end in range(start + 1, 90):
        a = range(start, end)
        if all((x in p) <= (((x in q) and (x not in a)) <= (x not in p)) for x in range(1, 100)):
            print(len(a))
            s.append(len(a))

print(min(s))

answer = 17

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(15, 1507, answer, '70efdf2ec9b086079795c442636b55fb'))