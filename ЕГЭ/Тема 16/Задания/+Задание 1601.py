def f(n):
    if n % 2 != 0 and n % 3 != 0:
        return 0
    if n % 2 == 0:
        return f(n // 2) + 3
    if n % 2 != 0 and n % 3 == 0:
        return f(n // 3) + 2
n = 15
print(f(n))
'''while True:
    if f(n) == 67:
        print(n)
        break
    n += 1'''


answer = 18874368
# 18874368
#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1601, answer, 'd43416548c620037459b5607111f8eb5'))