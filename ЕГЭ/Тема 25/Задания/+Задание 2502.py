def is_simp(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_divs(n):
    count_divs = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if is_simp(i):
                count_divs.add(i)
            if is_simp(n // i):
                count_divs.add(n // i)
    return sum(count_divs)


for i in range(1325000 - 1, 1324000, -1):
    divs = get_divs(i)
    if 0 < divs < 30000 and (divs % 5 == 0):
        print(i)
answer = [1324994, 1324992, 1324991, 1324986, 1324980]

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(25, 2502, answer, 'a4962eab53c004fe8f3ffaca3207d0fa'))