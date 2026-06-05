f = [0] * 1542613240
for n in range(765432015, 1542613240):
    if n > 0:
        f[n] = f[n // 10] + n % 10
count = 0
for i in range(len(f) - 1):
    if f[i] > f[i + 1]:
        count += 1
print(count)
answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1603, answer, '383d228fc45e55c06236b5d6278e1765'))