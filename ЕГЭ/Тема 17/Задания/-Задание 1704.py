list_val = list(int(x) for x in open('-Задание 1704.txt'))
min5 = min([x for x in list_val if x % 10 == 5])
count_pair = 0
min_sum = 10 ** 6
for i in range(len(list_val) - 1):
    pair = list_val[i:i + 2]
    if (100 <= pair[0] <= 999 and not(100 <= pair[1] <= 999)) or (100 <= pair[1] <= 999 and not(100 <= pair[0] <= 999)):
        if sum(pair) % min5:
            count_pair += 1
            min_sum = min(min_sum, sum(pair))

print(min5, count_pair, min_sum)

answer1 = 117
answer2 = 1639

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1704, f'{answer1} {answer2}', 'f3c45887478efcf9fcf722ab4708387d'))