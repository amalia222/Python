line = open('-Задание 2403.txt').readline()
left = 0
right = 1
vow = 'AEIOUY'
odd = '13579'
dig = '0123456789'
len_line = []
'''while len(line) > right:
    ch = line[left]
    if ch not in odd:
        right += 1
        left += 1
    else:
        while line[right] != line[left] or line[right] not in dig:
            right += 1
        if line[left - 1:right].isalpha() and sum([line[left - 1:right].count(x) for x in vow]) == len(line[left - 1:right]) // 2:
            len_line.append(line[left:right + 1])
        left = right + 1
        right += 1'''
while len(line) > left:
    ch = line[left]
    if ch not in odd:
        right += 1
        left += 1
    else:
        count_vow = 0
        count_con = 0
        while line[right].isalpha()



ans = max(len_line, key = len)
print(line.find(ans), ans)

answer = 521270

#

from tests.conftest import result_register

if answer is not Ellipsis:
    print(result_register(24, 2403, answer, '8f7d5fe843216dc768f4205b9c3867ed'))
