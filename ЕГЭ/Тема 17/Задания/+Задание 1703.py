list_val = list(int(x) for x in open('Задание 1703.txt'))
minn = min([x for x in list_val if str(x)[-1] == str(x)[-2]]) ** 2
count_pair = 0
max_sum = 0
for i in range(len(list_val) - 1):
    if str(list_val[i])[-1] == str(list_val[i + 1])[-2] or str(list_val[i])[-2] == str(list_val[i + 1])[-1]:
        if (list_val[i] % 13 == 0 and list_val[i + 1] % 13 != 0) or (list_val[i + 1] % 13 == 0 and list_val[i] % 13 != 0):
            if list_val[i] ** 2 + list_val[i + 1] ** 2 <= minn:
                count_pair += 1
                if max_sum < list_val[i] ** 2 + list_val[i + 1] ** 2:
                    max_sum = list_val[i] ** 2 + list_val[i + 1] ** 2
print(count_pair, max_sum, len(list_val))

answer1 = 115
answer2 = 96944186

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1703, f'{answer1} {answer2}', '1b1a3f384b8b6bddea7c6e63fad46024'))