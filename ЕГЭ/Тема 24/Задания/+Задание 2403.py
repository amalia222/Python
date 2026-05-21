line = open('-Задание 2403.txt').readline()
left = 0
right = 0
vow = 'AEIOUY'
odd = '13579'
dig = '0123456789'
max_len = 0
max_pos = -1
len_line = []
'''
while len(line) > right:
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
        right += 1
        
ans = max(len_line, key = len)
print(line.find(ans), ans)
'''

while len(line) > left:
    if line[left] not in odd:
        left += 1
    else:
        count_vow = 0
        count_con = 0
        right = left + 1

        while right < len(line) and line[right].isalpha():
            if line[right] in vow:
                count_vow += 1
            else:
                count_con += 1
            right += 1

        if right < len(line) and line[right] == line[left] and count_vow == count_con and count_vow > 0:
            length = right - left + 1
            if length > max_len or (max_len == length and left > max_pos):
                max_len = length
                max_pos = left

        left += 1

print(max_len, max_pos)

answer = 5165092

#

from tests.conftest import result_register

if answer is not Ellipsis:
    print(result_register(24, 2403, answer, '8f7d5fe843216dc768f4205b9c3867ed'))
