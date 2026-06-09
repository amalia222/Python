def divs(n):
    s = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return len(s)


s = []
for i in range(10 ** 9, 10 ** 8, -1):
    i_divs = divs(i)
    if (i - i_divs) % 23 == 0:
        s.append(i)
        if len(s) == 5:
            break

s.reverse()
print(s)
answer = s

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(25, 2503, answer, 'c867bc32545e94925e8d2198ad7333d9'))