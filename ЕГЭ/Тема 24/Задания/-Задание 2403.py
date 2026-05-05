line = open('Задание 2403.txt').readline()
line0 = line[::]
max_len = 0
ans = ''
for n in '0123456789':
    line0 = line0.replace(n, n + ' ' + n)

lines = line0.split()

for i in lines:
    if i[0] in '13579' and i[0] == i[-1]:
        if sum(i.count(ch) for ch in 'AEIOUY') == len(i) // 2:
            max_len = max(max_len, len(i))
            ans = i

print(line.find(ans))
answer = 521270

#

from tests.conftest import result_register

if answer is not Ellipsis:
    print(result_register(24, 2403, answer, '8f7d5fe843216dc768f4205b9c3867ed'))
