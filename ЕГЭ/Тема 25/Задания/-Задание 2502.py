def sumdel(n):
    s = {0}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return sum(s)

for n in range(1325000, 1300000, -1):
    s = sumdel(n)
    if 0 < s <= 30000 and s % 5 == 0:
        print(n)
answer = [1324991, 1324919, 1324891, 1324811, 1324601]

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(25, 2502, answer, 'a4962eab53c004fe8f3ffaca3207d0fa'))