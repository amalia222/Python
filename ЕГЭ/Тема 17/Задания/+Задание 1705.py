list_val = list(int(x) for x in open('Задание 1705.txt'))
max17 = max([x for x in list_val if x % 100 == 17])
count_triple = 0
max_sum = 0
for i in range(len(list_val) - 2):
    triple = list_val[i:i + 3]
    if sum([len(str(abs(x))) == 4 for x in triple]) == 2:
        if any(x % 5 == 0 for x in triple):
            if sum(triple) > max17:
                count_triple += 1
                max_sum = max(max_sum, sum(triple))

print(count_triple, max_sum)

answer1 = 21
answer2 = 114132

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1705, f'{answer1} {answer2}', 'e7eedde909e984c854776fabd948a26f'))