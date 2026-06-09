def is_simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True

def sum_del(n):
    s = set()
    count = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    for i in s:
        if is_simple(i):
            count += 1
    return sum(s), count

l = []
for i in range(4555705, 4600000):
    if i % 10 != 3:
        s, k = sum_del(i)
        if (i - s - k) % 100 == 23:
            l.append(i)
            if len(l) == 5:
                break

print(l)

# Ответ в виде списка чисел []
answer = l

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(25, 2504, answer, '4f6cb100db828c27d436322ae3bffeef'))