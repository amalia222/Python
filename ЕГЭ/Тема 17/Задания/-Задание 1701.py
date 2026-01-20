list_val = [int(x) for x in open('-Задание 1701.txt')]
count_pair = 0
min_sum = 10 ** 9
max9 = max(list_val, key = lambda x: -10000 < x < -1000 and abs(x) % 9 == 0)
print(max9)
for i in range(len(list_val) - 1):
    if list_val[i] * list_val[i + 1] < 0:
        if list_val[i] + list_val[i + 1] > max9:
            count_pair += 1
            if (list_val[i]) ** 2 + (list_val[i + 1]) ** 2 < min_sum:
                min_sum = (list_val[i]) ** 2 + (list_val[i + 1]) ** 2
print(count_pair, min_sum)
answer1 = 2851
answer2 = 504410

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1701, f'{answer1} {answer2}', 'b73de31c02e01cfc4508d15f2cf61e69'))