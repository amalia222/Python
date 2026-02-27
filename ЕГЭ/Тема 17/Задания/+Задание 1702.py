list_val = list(int(x) for x in open('+Задание 1702.txt'))
count_pair = 0
max_sum = 0
for i in range(len(list_val) - 1):
    for j in range(i + 1, len(list_val) - 1):
        if abs(list_val[i] - list_val[j]) % 60 == 0:
            if list_val[i] % 15 == 0 or list_val[j] % 15 == 0:
                count_pair += 1
                if list_val[i] - list_val[j] > max_sum:
                    max_sum = list_val[i] - list_val[j]
print(count_pair, max_sum)
answer1 = 63517
answer2 = 9960

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1702, f'{answer1} {answer2}', '1f1b321d4ee0f8a0a2de5ccf29035748'))