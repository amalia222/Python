line = open('-Задание 2402.txt').readline()
lines = line.replace('DE', '*').split('*')
max_len = 0
for i in range(len(lines)):
    line0 = 'DE'.join(lines[i:i + 241])
    if len(line0) > max_len:
        max_len = len(line0)

print(max_len)
answer = 970249

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(24, 2402, answer, '0bb01cf1951560939ce9d92c72dfd974'))